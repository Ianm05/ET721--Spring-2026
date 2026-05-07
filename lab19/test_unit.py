"""
Ian Martinez
May 5, 2026
lab 19: unit tests for verifying individual functions in a Flask-SQLite app
"""

import os
import sqlite3
import pytest
from app import app, get_db

#---------------------------------
# TEST DATABASE SETUP
#---------------------------------
TEST_DB = "test_flask_auth.db"

def init_test_db():
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@pytest.fixture
def db(monkeypatch):
    # override get_db to use test database
    def get_test_db():
        conn = sqlite3.connect(TEST_DB)
        conn.row_factory = sqlite3.Row
        return conn

    monkeypatch.setattr('app.get_db', get_test_db)
    init_test_db()

    yield get_test_db()

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

#---------------------------------
# TEST get_db RETURNS A CONNECTION
#---------------------------------
def test_get_db_returns_connection(db):
    # verify the database connection is a valid sqlite3 connection
    assert isinstance(db, sqlite3.Connection)

#---------------------------------
# TEST get_db ROW FACTORY
#---------------------------------
def test_get_db_row_factory(db):
    # verify rows are returned as sqlite3.Row objects (accessible by column name)
    assert db.row_factory == sqlite3.Row

#---------------------------------
# TEST INSERT USER INTO DATABASE
#---------------------------------
def test_insert_user(db):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO users (username, email, password) VALUES (?, ?, ?)""",
                   ("testuser", "test@example.com", "123456"))
    db.commit()

    cursor.execute("SELECT * FROM users WHERE email = ?", ("test@example.com",))
    user = cursor.fetchone()

    assert user is not None
    assert user["username"] == "testuser"
    assert user["email"] == "test@example.com"

#---------------------------------
# TEST DUPLICATE EMAIL IS REJECTED
#---------------------------------
def test_duplicate_email(db):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO users (username, email, password) VALUES (?, ?, ?)""",
                   ("user1", "dupe@example.com", "123456"))
    db.commit()

    # inserting the same email again should raise an IntegrityError
    with pytest.raises(sqlite3.IntegrityError):
        cursor.execute("""INSERT INTO users (username, email, password) VALUES (?, ?, ?)""",
                       ("user2", "dupe@example.com", "654321"))
        db.commit()

#---------------------------------
# TEST LOGIN QUERY - VALID USER
#---------------------------------
def test_login_query_valid(db):
    cursor = db.cursor()
    cursor.execute("""INSERT INTO users (username, email, password) VALUES (?, ?, ?)""",
                   ("loginuser", "login@example.com", "123456"))
    db.commit()

    # simulate the query used in the login route
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?",
                   ("login@example.com", "123456"))
    user = cursor.fetchone()

    assert user is not None
    assert user["username"] == "loginuser"

#---------------------------------
# TEST LOGIN QUERY - INVALID USER
#---------------------------------
def test_login_query_invalid(db):
    # simulate a login attempt with wrong credentials
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?",
                   ("wrong@example.com", "wrongpass"))
    user = cursor.fetchone()

    assert user is None

#---------------------------------
# TEST DASHBOARD REDIRECTS IF NOT LOGGED IN
#---------------------------------
def test_dashboard_redirects_if_not_logged_in():
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret'
    with app.test_client() as client:
        response = client.get('/dashboard')
        assert response.status_code == 302
        assert 'login' in response.location