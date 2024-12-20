import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Reading the collection
collection_ref = db.collection('users')
docs = collection_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')