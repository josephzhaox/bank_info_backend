import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
    
    # Firebase settings
    FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH')
    FIRESTORE_PROJECT_ID = os.getenv('FIRESTORE_PROJECT_ID')