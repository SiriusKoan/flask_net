from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from models import *
import time

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
        if request.method == 'GET':
            return render_template("login.html")
        if request.method == 'POST':
            username = request.form.get('username')
            passwd = request.form.get('passwd')
            status = authorize(username, passwd)
            return render_template('login.html', status=status)
            


if __name__ == "__main__":
        app.run(debug=True, host = "127.0.0.1", port="8082")
