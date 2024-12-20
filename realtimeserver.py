import firebase_admin
from firebase_admin import credentials, db

# Path to your service account key JSON file
cred = credentials.Certificate("serviceAccountKey.json")

# Initialize the Firebase Admin SDK
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://flask-firebase-practice-app-default-rtdb.firebaseio.com'
})

# Reference to the root of the database
ref = db.reference('/')

# Reading data from the database
data = ref.get()
print("Data from Firebase:", data)