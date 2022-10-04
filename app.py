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
    conn = get_db_connection()
    authors = conn.execute('SELECT * FROM author').fetchall()
    conn.close()
    if request.method == 'POST':
        id = request.form['id']
        authorid = request.form['authorid']
        title = request.form['title']
        if not title or not id or not authorid:
            flash('Something is missing!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO book (bookid,title,authorid) VALUES (?,?,?)',
                         (id,title,authorid))
            conn.commit()
            conn.close()
            return redirect(url_for('showbook'))

    return render_template('createbook.html',authors=authors)

@app.route('/createauthor', methods=('GET', 'POST'))
def createauthor():
    if request.method == 'POST':
        authorid = request.form['authorid']
        name = request.form['name']
        priority = request.form['priority']
        if not authorid or not name:
            flash('Something is missing!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO author (authorid,name,priority) VALUES (?,?,?)',
                         (authorid,name,priority))
            conn.commit()
            conn.close()
            return redirect(url_for('showauthor'))

    return render_template('createauthor.html')

@app.route('/<int:id>/editbook', methods=('GET', 'POST'))
def edit(bookid):
    post = get_post(bookid)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE book SET title = ?'
                         ' WHERE bookid = ?',
                         (title,bookid))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('editbook.html', post=post)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)