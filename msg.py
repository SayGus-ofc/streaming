import pyrebase
import time

config = {
    "apiKey": "AIzaSyAmay8dzxWVYh8JfCwuLtWBRf0bSeJjfjw",
  "authDomain": "login-6bd82.firebaseapp.com",
  "databaseURL": "https://login-6bd82.firebaseio.com",
  "projectId": "login-6bd82",
  "storageBucket": "login-6bd82.appspot.com",
  "messagingSenderId": "1050895485889",
  "appId": "1:1050895485889:web:96246e5052925037f8fd40",
  "measurementId": "G-T7DDQT8QH6"}

f = pyrebase.initialize_app(config)
db = f.database()
def adduser(msg):
    u = str(time.time())
    db.child("mensagens").child(u).set({"msg": msg})
    return 200