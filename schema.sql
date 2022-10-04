DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS author;
CREATE TABLE book (
    bookid INTEGER PRIMARY KEY ,
    title TEXT NOT NULL
);
CREATE TABLE author (
    authorid INTEGER PRIMARY KEY ,
    bookid TEXT NOT NULL,
    name TEXT NOT NULL,
    priority TEXT NOT NULL,
    FOREIGN KEY(bookid) REFERENCES book(bookid) 
);
