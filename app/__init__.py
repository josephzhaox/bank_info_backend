import os
from flask import Flask
from config import Config
from config import get_config
from .routes.auth import auth_bp
from .routes.banks import banks_bp

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Load configuration based on FLASK_ENV
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(get_config(env))

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(banks_bp, url_prefix='/api/banks')
    
    return app