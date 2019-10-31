DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT    NOT NULL,
    passwd   TEXT    NOT NULL,
    login_ip BINARY
);
