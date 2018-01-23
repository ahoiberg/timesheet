drop table if exists entries;
create table entries (
    id integer primary key autoincrement, 
    hours real not null,
    day date not null,
    comment text
);