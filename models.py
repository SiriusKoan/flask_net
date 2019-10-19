import sqlite3 as sql
from os import path
import encrypt
from flask import request

ROOT = path.dirname(path.relpath((__file__)))

def create_post(time, name, content):
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (time, name, content) values(?, ?, ?)', (time, name, content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'database_post.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts


def authorize(username, passwd):
    con = sql.connect(path.join(ROOT, "database_user.db"))
    cur = con.cursor()
    cur.execute('select * from users')
    data = cur.fetchall()
    for user in data:
        if username in user:
            p = user[2]
      
    try:
        if encrypt.sha(passwd) == p:
            cur.execute("update users set login_ip = '%s' where username = '%s'" %(request.remote_addr, username))
            con.commit()
            con.close()
            return "login successfully!"
        else:
            return "login failed..."
    except:
        return "There's not this user..."
    



def register(username, passwd):
    con = sql.connect(path.join(ROOT, "database_user.db"))
    cur = con.cursor()
    cur.execute('select username from users')
    data = cur.fetchall()
    all_users = []
    for user in data:
        all_users.append(user[0])

    if username in all_users:
        return "Username " + username + " exists..."
    else:
        cur.execute('insert into users (username, passwd) values(?, ?)', (username, encrypt.sha(passwd)))
        con.commit()
        con.close()
        return "create " + username + " successfully!"
