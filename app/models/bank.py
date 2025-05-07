# Bank data model for Firestore
class Bank:
    def __init__(self, id, name, address, phone, user_id):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.user_id = user_id  # Associate bank with user
    
    # Convert to dict for Firestore
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'user_id': self.user_id
        }
    
    # Create from Firestore document
    @staticmethod
    def from_dict(data):
        return Bank(
            id=data['id'],
            name=data['name'],
            address=data['address'],
            phone=data['phone'],
            user_id=data['user_id']
        )