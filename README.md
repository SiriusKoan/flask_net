# flask_net
<img alt="GitHub" src="https://img.shields.io/github/license/SiriusKoan/flask_net">

## Setup

1. Modify the IP address and port in `app.py` at line 63.
2. Modify the IP address(url) and port in the `main`, `register`, `login` and `logout` block.
3. Run the following command to create the `users` and `posts` databases.
```sh
$ sqlite3 user.db < schema_user.sql
$ sqlite3 post.db < schema_post.sql
```
4. Run the command below to create a user named `root` with administrator privileges.
**Attention**: the `password_hash` should be encrypted by `encrypt.py` in this project, which will create a sha1 hash.
```sql
INSERT INTO users (username, passwd) VALUES (?, ?), ("root", "password_hash")
```

## Deploy

- Modify the IP and port in the command below.
- You can use certbot to generate `cert.pem` and `privikey.pem` file.

```sh
$ pip install -r requirements.txt
$ flask run --cert=key/cert.pem --key=key/privkey.pem --port 443 --host 140.131.149.50
```
