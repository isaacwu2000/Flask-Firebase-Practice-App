from firebase import firebase
firebase = firebase.FirebaseApplication('https://flask-firebase-practice-app-default-rtdb.firebaseio.com/', None)

@app.route("/")
def home():
  result = firebase.get('/restaurants', None)
  return str(result)