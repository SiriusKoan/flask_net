from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from models import *
import time

app = Flask(__name__)
CORS(app)

# main
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(time.ctime(time.time()), name, post)

    posts = get_posts()

    who = who_login(request.remote_addr)
    if who != "haven't login":
        return render_template('index.html', posts = posts, who = who[0])
    else:
        return render_template('index.html', posts = posts, who = who)

# register
@app.route('/register', methods = ['GET', 'POST'])
def register_main():
    if request.method == 'GET':
        return render_template("register.html", status = "")
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        status = register(username, passwd)
        if "successfully!" in status:
            return redirect("/login")
        else:
            return render_template('register.html', status = status)

# login
@app.route('/login', methods = ['GET', 'POST'])
def login_main():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        status = authorize(username, passwd)
        if status == "login successfully!":
            return redirect("/")
        else:
            return render_template('login.html', status = status)

# logout
@app.route("/logout")
def logout_main():
    logout(request.remote_addr)
    return redirect("/")

# admin
@app.route("/admin")
def admin_manage():
    users = make_table(show_users())
    posts = make_table(show_posts())
    whether_root = True if "root" in who_login(request.remote_addr) else False
    return render_template('admin.html', users = users, posts = posts, whether_root = whether_root)



if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = "8080", debug = True)
