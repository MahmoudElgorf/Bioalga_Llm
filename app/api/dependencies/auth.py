"""
Authentication and Authorization Dependencies
Handles API key validation, user authentication, and request authorization
"""

from fastapi import Request, HTTPException, Security, Depends, Query, Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, APIKeyHeader, APIKeyQuery
from typing import Optional, Dict, Any
import os
import secrets
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

# Configuration
API_KEY = os.getenv("API_KEY", "")
REQUIRE_AUTH = os.getenv("REQUIRE_AUTH", "false").lower() == "true"
API_KEY_NAME = os.getenv("API_KEY_NAME", "X-API-Key")

# Security schemes
security = HTTPBearer(auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_query = APIKeyQuery(name="api_key", auto_error=False)


class ApiKeyHeader:
    """API Key authentication via header"""
    async def __call__(self, api_key: str = Security(api_key_header)) -> str:
        if not api_key:
            raise HTTPException(
                status_code=403,
                detail=f"Missing API Key in header: {API_KEY_NAME}"
            )
        return api_key


class ApiKeyQuery:
    """API Key authentication via query parameter"""
    async def __call__(self, api_key: str = Security(api_key_query)) -> str:
        if not api_key:
            raise HTTPException(
                status_code=403,
                detail=f"Missing API Key in query parameter: api_key"
            )
        return api_key


def verify_api_key(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(security),
    header_key: str = Security(api_key_header),
    query_key: str = Security(api_key_query)
) -> bool:
    """
    Verify API key from multiple sources:
    - Bearer token header
    - X-API-Key header
    - api_key query parameter
    
    Returns:
        True if API key is valid or auth not required
    
    Raises:
        HTTPException 403 if key is invalid
    """
    # If authentication is disabled, allow all requests
    if not REQUIRE_AUTH or not API_KEY:
        logger.debug("Authentication is disabled")
        return True
    
    # Try to get key from various sources
    provided_key = None
    
    # Check Bearer token
    if credentials and credentials.credentials:
        provided_key = credentials.credentials
    
    # Check custom header
    if not provided_key and header_key:
        provided_key = header_key
    
    # Check query parameter
    if not provided_key and query_key:
        provided_key = query_key
    
    # Validate the key
    if provided_key and provided_key == API_KEY:
        logger.info("Authentication successful")
        return True
    
    # Authentication failed
    logger.warning(f"Authentication failed for key: {provided_key[:10] if provided_key else 'None'}...")
    raise HTTPException(
        status_code=403,
        detail="Invalid or missing API Key",
        headers={
            "WWW-Authenticate": "Bearer",
            "X-API-Key-Required": API_KEY_NAME
        }
    )


def optional_auth(
    request: Request,
    credentials: Optional[HTTPAuthorizationCredentials] = Security(security),
    header_key: str = Security(api_key_header),
    query_key: str = Security(api_key_query)
) -> bool:
    """
    Optional authentication - doesn't block if no key provided
    
    Returns:
        True if authenticated, False otherwise
    """
    if not REQUIRE_AUTH or not API_KEY:
        return True
    
    # Try to get key
    provided_key = None
    if credentials and credentials.credentials:
        provided_key = credentials.credentials
    elif header_key:
        provided_key = header_key
    elif query_key:
        provided_key = query_key
    
    # Set auth status in request state
    is_authenticated = (provided_key == API_KEY)
    request.state.is_authenticated = is_authenticated
    
    if is_authenticated:
        request.state.user = {"id": "api_user", "type": "api_key"}
    
    return is_authenticated


def get_current_user(
    authenticated: bool = Depends(optional_auth),
    request: Request = None
) -> Optional[Dict[str, Any]]:
    """
    Get current authenticated user information
    
    Returns:
        User dict if authenticated, None otherwise
    """
    if not authenticated:
        return None
    
    if request and hasattr(request, 'state') and hasattr(request.state, 'user'):
        return request.state.user
    
    return {"id": "api_user", "type": "api_key", "authenticated": True}


def require_auth(
    authenticated: bool = Depends(verify_api_key)
) -> bool:
    """
    Require authentication for endpoint
    
    This is a wrapper that enforces authentication
    """
    return authenticated


# For endpoints that need rate limiting per user
class RateLimitDependency:
    """Rate limiting dependency that uses user ID or IP"""
    
    def __init__(self, requests_per_minute: int = 60):
        self.requests_per_minute = requests_per_minute
        self._requests = {}
    
    async def __call__(
        self,
        request: Request,
        authenticated: bool = Depends(optional_auth)
    ) -> bool:
        """
        Check rate limit for current user/IP
        
        Returns:
            True if within limit
        
        Raises:
            HTTPException 429 if exceeded
        """
        # Get identifier (user ID or IP)
        if authenticated and hasattr(request.state, 'user'):
            identifier = f"user_{request.state.user.get('id', 'unknown')}"
        else:
            identifier = request.client.host if request.client else "unknown"
        
        # Clean old requests
        now = datetime.now()
        if identifier not in self._requests:
            self._requests[identifier] = []
        
        # Remove requests older than 1 minute
        self._requests[identifier] = [
            req_time for req_time in self._requests[identifier]
            if (now - req_time).seconds < 60
        ]
        
        # Check limit
        if len(self._requests[identifier]) >= self.requests_per_minute:
            raise HTTPException(
                status_code=429,
                detail=f"Rate limit exceeded. Maximum {self.requests_per_minute} requests per minute."
            )
        
        # Add current request
        self._requests[identifier].append(now)
        
        return True


def generate_api_key() -> Dict[str, str]:
    """
    Generate a secure API key
    
    Returns:
        Dictionary with generated key and metadata
    """
    key = secrets.token_urlsafe(32)
    return {
        "api_key": key,
        "type": "bearer_token",
        "created_at": datetime.now().isoformat(),
        "note": "Store this key securely. You cannot retrieve it again."
    }


def validate_api_key_format(api_key: str) -> bool:
    """
    Validate API key format
    
    Args:
        api_key: The API key to validate
    
    Returns:
        True if format is valid
    """
    if not api_key or len(api_key) < 10:
        return False
    
    # API keys should be alphanumeric with hyphens/underscores
    import re
    pattern = r'^[A-Za-z0-9\-_]+$'
    return bool(re.match(pattern, api_key))


# Pre-configured rate limiting instances
rate_limit_strict = RateLimitDependency(requests_per_minute=30)
rate_limit_medium = RateLimitDependency(requests_per_minute=60)
rate_limit_loose = RateLimitDependency(requests_per_minute=120)