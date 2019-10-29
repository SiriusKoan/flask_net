# flask_net

Made by Sirius

## set

Before use, you have to modify the IP address and port in app.py line 63. After that, you also need to modify the IP address(url) and port you just set in the main, register, login and logout block.
Then you should run the following two command to create database of users and posts.

```sh
$ sqlite3 database_user.db < schema_user.sql
```

```sh
$ sqlite3 database_post.db < schema_post.sql
```

Finally, you have to run this command to add "root" as the admin(texts are red), or the username may be registered by others. The encrypt_password should be encrypted by the program named encrypt.py in this project, we use sha1 to encrypt.

```sql
insert into users (username, passwd) values(?, ?)', ("root", "encrypt_password")
```

## run

app.py is the main program, you only need to run it.
