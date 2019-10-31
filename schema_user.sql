drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username text not null,
    passwd text not null,
    login_ip binary
);
