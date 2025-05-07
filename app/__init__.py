from flask import Flask
from config import Config
from .routes.auth import auth_bp
from .routes.banks import banks_bp

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(banks_bp, url_prefix='/api/banks')
    
    return app