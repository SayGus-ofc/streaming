from flask import Flask, render_template
from flask import request
from time import time
import msg
import os


app = Flask(__name__,template_folder="")
app.debug=True


@app.route("/")
def init():
    return render_template("yn.html")
    
    
    
@app.route('/response', methods=["POST"])
def response():
    data = request.form["msg"]
    msg.adduser(data)
    return render_template("yn2.html")
    
    
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
