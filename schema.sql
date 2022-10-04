DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS author;

CREATE TABLE author (
    authorid INTEGER PRIMARY KEY ,
    name TEXT NOT NULL,
    priority TEXT NOT NULL
);
CREATE TABLE book (
    bookid INTEGER PRIMARY KEY ,
    title TEXT NOT NULL,
    authorid INTEGER,
    FOREIGN KEY(authorid) REFERENCES author(authorid)
);
