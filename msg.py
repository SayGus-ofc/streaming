import pyrebase
from random import randint

config = {
  "authDomain": "fir-e65af.firebaseapp.com",
  "projectId": "fir-e65af",
  "storageBucket": "fir-e65af.appspot.com",
  "messagingSenderId": "216052591088",
  "appId": "1:216052591088:web:f3b865fb51ec77d2eb9535"
};

f = pyrebase.initialize_app(config)
db = f.database()
def adduser(msg):
    u = str(randint(0,99999))
    db.child(u).set({"msg": msg})
    return 200
