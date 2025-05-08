from flask import Blueprint, request, jsonify
from ..models.bank import Bank
from ..services.firestore_service import FirestoreService
from ..utils.middleware import require_auth
from uuid import uuid4

banks_bp = Blueprint('banks', __name__)
firestore_service = FirestoreService(project_id='bankinfoapp')  # Replace with your project ID

# Create a bank
@banks_bp.route('/', methods=['POST'])
@require_auth
def create_bank():
    print("DEBUG: Entering create_bank route")
    data = request.get_json()
    print(f"DEBUG: Request JSON: {data}")

    if not all(key in data for key in ['name', 'address', 'phone']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    bank = Bank(
        id=str(uuid4()),
        name=data['name'],
        address=data['address'],
        phone=data['phone'],
        user_id=request.user_id
    )
    saved_bank = firestore_service.save_bank(bank)
    return jsonify(saved_bank.to_dict()), 201

# Read banks (search by name)
@banks_bp.route('/', methods=['GET'])
@require_auth
def search_banks():
    print(f"DEBUG: Entering search_banks, request: {request}")

    query = request.args.get('query', '')
    print(f"DEBUG: Query parameter: {query}")
    try:
        banks = firestore_service.search_banks(query, request.user_id)
        return jsonify([bank.to_dict() for bank in banks]), 200
    except Exception as e:
        print(f"DEBUG: Error in search_banks: {str(e)}")
        return jsonify({'error': f"Search failed: {str(e)}"}), 500

# Update a bank
@banks_bp.route('/<bank_id>', methods=['PUT'])
@require_auth
def update_bank(bank_id):
    data = request.get_json()
    bank = firestore_service.get_bank(bank_id)
    if not bank or bank.user_id != request.user_id:
        return jsonify({'error': 'Bank not found or unauthorized'}), 404
    
    bank.name = data.get('name', bank.name)
    bank.address = data.get('address', bank.address)
    bank.phone = data.get('phone', bank.phone)
    saved_bank = firestore_service.save_bank(bank)
    return jsonify(saved_bank.to_dict()), 200

# Delete a bank
@banks_bp.route('/<bank_id>', methods=['DELETE'])
@require_auth
def delete_bank(bank_id):
    bank = firestore_service.get_bank(bank_id)
    if not bank or bank.user_id != request.user_id:
        return jsonify({'error': 'Bank not found or unauthorized'}), 404
    
    firestore_service.delete_bank(bank_id)
    return jsonify({'message': 'Bank deleted'}), 200