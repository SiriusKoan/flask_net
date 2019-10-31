import sqlite3 as sql
from os import path
import encrypt
from flask import request

ROOT = path.dirname(path.relpath((__file__)))

# main
def create_post(time, name, content):
    con = sql.connect(path.join(ROOT, 'post.db'))
    cur = con.cursor()
    if name != '' and content != '':
        cur.execute('INSERT INTO posts (time, name, content) VALUES (?, ?, ?)', (time, name, content))
        con.commit()
        con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'post.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM posts')
    posts = cur.fetchall()
    return posts

def who_login(remote_ip):
    con = sql.connect(path.join(ROOT, 'user.db'))
    cur = con.cursor()
    cur.execute('SELECT login_ip FROM users')
    ips = cur.fetchall()
    for ip in ips:
        if ip[0] == remote_ip:
            cur.execute('SELECT USERNAME FROM users WHERE login_ip = "?"', (ip))
            who = cur.fetchall()
            con.commit()
            con.close()
            return who[0]
    con.commit()
    con.close()
    return ''

def logout(remote_ip):
    con = sql.connect(path.join(ROOT, 'user.db'))
    cur = con.cursor()
    cur.execute('SELECT login_ip FROM users')
    ips = cur.fetchall()
    for ip in ips:
        if ip[0] == remote_ip:
            cur.execute('UPDATE users SET login_ip = "" WHERE login_ip = "?"', (ip))
            con.commit()
            con.close()
            return True
    con.commit()
    con.close()
    return False


# login
def authorize(username, passwd):
    con = sql.connect(path.join(ROOT, 'user.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    data = cur.fetchall()
    for user in data:
        if username in user:
            p = user[2]

    try:
        if encrypt.sha(passwd) == p:
            cur.execute('UPDATE users SET login_ip = "?" WHERE username = "?"', (request.remote_addr, username))
            con.commit()
            con.close()
            return (True, 'login successfully!')
        else:
            return (False, 'login failed...')
    except:
        return (False, 'This user does not exist...')


# register
def register(username, passwd):
    con = sql.connect(path.join(ROOT, 'user.db'))
    cur = con.cursor()
    cur.execute('SELECT username FROM users')
    data = cur.fetchall()
    all_users = [user[0] for user in data]

    if username in all_users:
        return False
    else:
        cur.execute('INSERT INTO users (username, passwd) VALUES (?, ?)', (username, encrypt.sha(passwd)))
        con.commit()
        con.close()
        return True


# admin
def show_posts():
    con = sql.connect(path.join(ROOT, 'post.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM posts')
    data = cur.fetchall()
    con.close()
    return data

def show_users():
    con = sql.connect(path.join(ROOT, 'user.db'))
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    data = cur.fetchall()
    con.close()
    return data

def make_table(li):
    return '?'.join(''.join(str(it)) for it in li)

def announce(content):
    pass

def delete(db, primary):
    if db == 'u':
        con = sql.connect(path.join(ROOT, 'user.db'))
        cur = con.cursor()
        cur.execute('DELETE FROM users WHERE id = ?', (primary))
    if db == 'p':
        con = sql.connect(path.join(ROOT, 'post.db'))
        cur = con.cursor()
        cur.execute('DELETE FROM posts WHERE id = ?', (primary))
    con.commit()
    con.close()
