from firebase_admin import auth
from flask import abort

# Firebase authentication service
class AuthService:
    @staticmethod
    def verify_token(token):
        try:
            # Verify Firebase JWT token
            decoded_token = auth.verify_id_token(token)
            return decoded_token['uid']  # Return user ID
        except Exception as e:
            abort(401, description=f"Invalid token: {str(e)}")