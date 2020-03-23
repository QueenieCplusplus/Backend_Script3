import pyrebase
import GooPy


import pyrebase

config = {
  # "apiKey": "AIzaSyClr4KhSkUVy0kMipcXCYMCMpDCFgBEXKY", // shall have key
  "authDomain": "pattys-goopy-1527579295440.firebaseapp.com",
  "databaseURL": "https://pattys-goopy-1527579295440.firebaseio.com",
  "storageBucket": "pattys-goopy-1527579295440.appspot.com",
  "messagingSenderId": "557738520788"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
db.child("users").child("Pattys Lab")

data = {"distance":GooPy.distances}
db.child("How far now").push(data)