import os
from firebase_admin import auth
from flask import abort
from config import get_config
import firebase_admin

# Initialize Firebase if not already initialized
config = get_config(os.getenv('FLASK_ENV', 'development'))
if not firebase_admin._apps:
    cred = firebase_admin.credentials.Certificate(config.FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)


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