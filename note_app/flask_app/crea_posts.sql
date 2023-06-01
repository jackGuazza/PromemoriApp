drop table if exists posts;

create table posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT,
    info TEXT
);

insert into posts(titolo, info) values(
    'ttt1',
    'iii1'
);
insert into posts(titolo, info) values(
    'ttt2',
    'iii2'
);
insert into posts(titolo, info) values(
    'ttt3',
    'iii3'
);

