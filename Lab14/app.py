"""
Ian Martinez
lab 14, mini blog app using Flask
March 19, 2026
"""
from flask import Flask, render_template, redirect, url_for, request
import mysql.connector

app = Flask(__name__)

# database connection
db = mysql.connector.connect(
    host='127.0.0.1',
    user='flaskuser',
    password='password123',
    database='blogsDB'
)

# create cursor
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_blog', methods=['POST'])
def add_blog():
    username = request.form['username']
    email = request.form['email']
    title = request.form['title']
    content = request.form['content']   # ✅ fixed

    # insert into users table
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (%s, %s)",
        (username, email)
    )
    db.commit()

    # get last inserted user id
    user_id = cursor.lastrowid

    # insert into blog table
    cursor.execute(
        "INSERT INTO blog (user_id, title, content) VALUES (%s, %s, %s)",
        (user_id, title, content)
    )
    db.commit()

    return redirect(url_for('blogs'))  # cleaner redirect


@app.route('/blogs')
def blogs():
    cursor.execute("""
        SELECT blog.id, users.username, blog.title, blog.content, blog.created_at
        FROM blog
        JOIN users ON blog.user_id = users.id
    """)

    data = cursor.fetchall()

    return render_template('blogs.html', blogs=data)


if __name__ == '__main__':
    app.run(debug=True)