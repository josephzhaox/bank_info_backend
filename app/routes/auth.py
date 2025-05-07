from flask import Blueprint, jsonify

auth_bp = Blueprint('auth', __name__)

# Route to verify token (for testing or frontend integration)
@auth_bp.route('/verify', methods=['POST'])
def verify_token():
    return jsonify({'message': 'Token verification endpoint (handled by Firebase)'})