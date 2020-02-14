from flask import Flask, render_template, request, redirect
from flask_cors import CORS
from flaskext.markdown import Markdown
from models import *
import time

app = Flask(__name__)
CORS(app)
Markdown(app)

# main
@app.route('/', methods = ['GET', 'POST'])
def index():
    who = who_login(request.remote_addr)
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(time.ctime(time.time()), name, post, who)

    posts = get_posts()

    if who != '':
        return render_template('index.html', posts = posts, who = who[0])
    else:
        return render_template('index.html', posts = posts, who = who)

# register
@app.route('/register', methods = ['GET', 'POST'])
def register_main():
    if request.method == 'GET':
        return render_template('register.html', status = '')
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        success = register(username, passwd)
        if success:
            return redirect('/login')
        else:
            return render_template('register.html', status = 'Username exists!')

# login
@app.route('/login', methods = ['GET', 'POST'])
def login_main():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form.get('username')
        passwd = request.form.get('passwd')
        status, err_msg = authorize(username, passwd)
        if status:
            return redirect('/')
        else:
            return render_template('login.html', status = err_msg)

# logout
@app.route('/logout')
def logout_main():
    logout(request.remote_addr)
    return redirect('/')

# admin
@app.route('/admin', methods = ['GET', 'POST'])
def admin_manage():
    if request.method == 'GET':
        users = make_table(show_users())
        posts = make_table(show_posts())
        whether_root = 'root' in who_login(request.remote_addr)
        return render_template('admin.html', users = users, posts = posts, whether_root = whether_root)
    if request.method == 'POST':
        db = request.form.get('primary')[0]
        primary = request.form.get('primary')[1]
        delete(db, primary)
        return redirect('/admin')

@app.route('/admin/delete')
def delete_post_or_user():
    primary_key = request.form.get('primary')
    delete(primary_key)
    


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8080, debug = True)
