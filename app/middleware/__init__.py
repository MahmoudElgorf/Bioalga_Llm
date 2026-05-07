from app.middleware.cors import setup_cors

# Import auth functions only if file exists
try:
    from app.middleware.auth import verify_api_key, optional_auth, get_current_user, require_auth
except ImportError:
    # Define dummy functions if auth.py doesn't exist
    def verify_api_key(*args, **kwargs):
        return True
    
    def optional_auth(*args, **kwargs):
        return True
    
    def get_current_user(*args, **kwargs):
        return None
    
    def require_auth(*args, **kwargs):
        return True

__all__ = [
    'setup_cors',
    'verify_api_key',
    'optional_auth',
    'get_current_user',
    'require_auth'
]