from flask import Flask, request, flash, url_for, redirect, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/book')
def showbook():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM book').fetchall()
    conn.close()
    return render_template('show_book.html', books=books)

@app.route('/author')
def showauthors():
    conn = get_db_connection()
    authors = conn.execute('SELECT * FROM author').fetchall()
    conn.close()
    return render_template('show_author.html', authors=authors)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()