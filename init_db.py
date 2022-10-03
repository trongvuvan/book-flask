import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO book (bookid, title) VALUES (?, ?)",
            ('1', 'The lord of the gay')
            )

cur.execute("INSERT INTO book (bookid, title) VALUES (?, ?)",
            ('2', 'Gay lord')
            )
cur.execute("INSERT INTO author (authorid, bookid,name,priority) VALUES (?, ?,?,?)",
            ('1', '2','Gay Author','nope')
            )
connection.commit()
connection.close()
