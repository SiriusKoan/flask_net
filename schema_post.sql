drop table if exists posts;
create table posts (
    id integer primary key autoincrement,
    time text not null,
    name text not null,
    content text not null
);
