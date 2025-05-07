import os
from dotenv import load_dotenv
## print(os.getenv('FIREBASE_CREDENTIALS_PATH'))  # Should print: C:\Users\YourUsername\secure\firebase-service-account.json
# Load environment variables from .env file
load_dotenv()

class Config:
    """Base configuration class."""
    # Flask settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')  # Fallback for development
    DEBUG = True  # Default to False for production safety
    
    # Firebase settings
    FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH')
    FIRESTORE_PROJECT_ID = os.getenv('FIRESTORE_PROJECT_ID')
    
    def __init__(self):
        """Validate required configurations."""
        if not self.SECRET_KEY or self.SECRET_KEY == 'default-secret-key':
            print("Warning: Using default SECRET_KEY. Set a secure SECRET_KEY in .env for production.")
        if not self.FIREBASE_CREDENTIALS_PATH:
            raise ValueError("FIREBASE_CREDENTIALS_PATH must be set in .env")
        if not self.FIRESTORE_PROJECT_ID:
            raise ValueError("FIRESTORE_PROJECT_ID must be set in .env")

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    
    # For production, override FIREBASE_CREDENTIALS_PATH with Secret Manager (optional)
    FIREBASE_CREDENTIALS_PATH = os.getenv('FIREBASE_CREDENTIALS_PATH', './google-services.json')

# Map environments to configurations
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

def get_config(env='development'):
    """Get configuration based on environment."""
    return config_by_name.get(env, DevelopmentConfig)()