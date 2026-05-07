"""
Authentication Middleware
Handles API key validation and request authentication
"""

from fastapi import Request, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, APIKeyHeader, APIKeyQuery
from typing import Optional
import os
import secrets

# Configuration
API_KEY = os.getenv("API_KEY", "")
REQUIRE_AUTH = os.getenv("REQUIRE_AUTH", "false").lower() == "true"
API_KEY_NAME = os.getenv("API_KEY_NAME", "X-API-Key")

# Security schemes
security = HTTPBearer(auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
api_key_query = APIKeyQuery(name="api_key", auto_error=False)


def verify_api_key(
    credentials: Optional[HTTPAuthorizationCredentials] = Security(security),
    header_key: str = Security(api_key_header),
    query_key: str = Security(api_key_query)
) -> bool:
    """
    Verify API key from multiple sources
    """
    if not REQUIRE_AUTH or not API_KEY:
        return True
    
    provided_key = None
    
    if credentials and credentials.credentials:
        provided_key = credentials.credentials
    elif header_key:
        provided_key = header_key
    elif query_key:
        provided_key = query_key
    
    if provided_key and provided_key == API_KEY:
        return True
    
    raise HTTPException(
        status_code=403,
        detail="Invalid or missing API Key"
    )


def optional_auth(
    request: Request,
    credentials: Optional[HTTPAuthorizationCredentials] = Security(security),
    header_key: str = Security(api_key_header),
    query_key: str = Security(api_key_query)
) -> bool:
    """
    Optional authentication - doesn't block if no key provided
    """
    if not REQUIRE_AUTH or not API_KEY:
        return True
    
    provided_key = None
    if credentials and credentials.credentials:
        provided_key = credentials.credentials
    elif header_key:
        provided_key = header_key
    elif query_key:
        provided_key = query_key
    
    is_authenticated = (provided_key == API_KEY)
    request.state.is_authenticated = is_authenticated
    
    if is_authenticated:
        request.state.user = {"id": "api_user", "type": "api_key"}
    
    return is_authenticated


def get_current_user(request: Request) -> Optional[dict]:
    """Get current authenticated user"""
    if hasattr(request.state, 'user'):
        return request.state.user
    return None


def require_auth(authenticated: bool = Security(verify_api_key)) -> bool:
    """Require authentication for endpoint"""
    return authenticated


def generate_api_key() -> dict:
    """Generate a secure API key"""
    key = secrets.token_urlsafe(32)
    return {
        "api_key": key,
        "type": "bearer_token",
        "created_at": __import__('datetime').datetime.now().isoformat()
    }


def validate_api_key_format(api_key: str) -> bool:
    """Validate API key format"""
    if not api_key or len(api_key) < 10:
        return False
    import re
    pattern = r'^[A-Za-z0-9\-_]+$'
    return bool(re.match(pattern, api_key))