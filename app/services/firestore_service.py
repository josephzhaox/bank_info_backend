from firebase_admin import firestore
from ..models.bank import Bank

# Firestore database service
class FirestoreService:
    def __init__(self, project_id):
        self.db = firestore.client()
        self.project_id = project_id
    
    # Create or update a bank
    def save_bank(self, bank):
        doc_ref = self.db.collection('banks').document(bank.id)
        doc_ref.set(bank.to_dict())
        return bank
    
    # Get a bank by ID
    def get_bank(self, bank_id):
        doc_ref = self.db.collection('banks').document(bank_id)
        doc = doc_ref.get()
        if doc.exists:
            return Bank.from_dict(doc.to_dict())
        return None
    
    # Search banks by name (partial match) for a user
    def search_banks(self, query, user_id):
        query_ref = (self.db.collection('banks')
                     .where('user_id', '==', user_id)
                     .where('name', '>=', query)
                     .where('name', '<=', query + '\uf8ff'))
        docs = query_ref.get()
        return [Bank.from_dict(doc.to_dict()) for doc in docs]
    
    # Delete a bank
    def delete_bank(self, bank_id):
        doc_ref = self.db.collection('banks').document(bank_id)
        doc_ref.delete()