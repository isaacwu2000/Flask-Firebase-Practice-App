import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Reading the collection
collection_ref = db.collection('users')
docs = collection_ref.stream()

# Converting the docs into a list of dictionaries
languages = []
for doc in docs:
    language = doc.to_dict()
    language['name'] = doc.id
    languages.append(language)
print(languages)