from flask import Flask, request, flash, url_for, redirect, render_template
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/book')
def showbook():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM book').fetchall()
    authors = conn.execute('SELECT * FROM author').fetchall()
    conn.close()
    return render_template('show_book.html', books=books,authors=authors)

@app.route('/author')
def showauthor():
    conn = get_db_connection()
    authors = conn.execute('SELECT * FROM author').fetchall()
    books = conn.execute('SELECT * FROM book').fetchall()
    conn.close()
    return render_template('show_author.html', authors=authors,books=books)

@app.route('/createbook', methods=('GET', 'POST'))
def createbook():
    if request.method == 'POST':
        id = request.form['id']
        title = request.form['title']
        if not title or not id:
            flash('Something is missing!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO book (bookid,title) VALUES (?,?)',
                         (id,title))
            conn.commit()
            conn.close()
            return redirect(url_for('showbook'))

    return render_template('createbook.html')

@app.route('/createauthor', methods=('GET', 'POST'))
def createauthor():
    if request.method == 'POST':
        authorid = request.form['authorid']
        bookid = request.form['bookid']
        name = request.form['name']
        priority = request.form['priority']
        if not authorid or not bookid or not name:
            flash('Something is missing!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO author (authorid,bookid,name,priority) VALUES (?,?,?,?)',
                         (authorid,bookid,name,priority))
            conn.commit()
            conn.close()
            return redirect(url_for('showauthor'))

    return render_template('createauthor.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()