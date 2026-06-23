from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('portfolio.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    projects = conn.execute('SELECT * FROM projects').fetchall()
    conn.close()

    return render_template('index.html', projects=projects)

@app.route('/admin')
def admin():
    conn = get_db_connection()
    projects = conn.execute('SELECT * FROM projects').fetchall()
    conn.close()

    return render_template('admin.html', projects=projects)

@app.route('/add', methods=['POST'])
def add_project():
    title = request.form['title']
    description = request.form['description']

    conn = get_db_connection()
    conn.execute(
        'INSERT INTO projects (title, description) VALUES (?, ?)',
        (title, description)
    )
    conn.commit()
    conn.close()

    return redirect('/admin')

@app.route('/delete/<int:id>')
def delete_project(id):
    conn = get_db_connection()

    conn.execute(
        'DELETE FROM projects WHERE id=?',
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/admin')

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)