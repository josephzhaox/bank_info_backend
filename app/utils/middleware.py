from flask import request, abort
from functools import wraps
from ..services.auth_service import AuthService

# JWT middleware for protected routes
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            abort(401, description="Missing or invalid Authorization header")
        
        token = auth_header.split(' ')[1]
        user_id = AuthService.verify_token(token)
        request.user_id = user_id  # Attach user_id to request
        return f(*args, **kwargs)
    
    return decorated