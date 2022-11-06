from flask import Flask
from flask import request
import os


app = Flask(__name__)
app.debug=True


@app.route("/")
def init():
    ip = request.environ['REMOTE_ADDR']
    return ip
    
    
@app.route('/register/<resp>')
def register(resp):
    return resp
    
    
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
