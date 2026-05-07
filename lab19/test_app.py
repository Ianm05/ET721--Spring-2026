"""
Ian Martinez
May, 5 , 2026
lab 19: unit test for verifying authentication in a Flask-sQlite app
"""

import os
import sqlite3
import pytest
from app import app
#---------------------------------
# TEST DATABASE SETUP
#---------------------------------
TEST_DB = "test_flask_auth.db"

def init_test_db():
    #simulate a database connection
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()

    # create a temple table
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

# create a mock database to run the app.py file
@pytest.fixture
def client(monkeypatch):
    # override database to use test database
    def get_test_db():
        conn = sqlite3.connect(TEST_DB)
        conn.row_factory = sqlite3.Row
        return conn

    # match the mock database
    from app import get_db
    monkeypatch.setattr('app.get_db', get_test_db)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret'

    # call function to run the mock database
    init_test_db()

    with app.test_client() as client:
        yield client

    # cleanup test database after tests
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

#---------------------------------
# TEST HOME REDIRECT
#---------------------------------
def test_home_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
    assert 'login' in response.location

#---------------------------------
# TEST LOGIN SUCCESS
#---------------------------------
def test_login_success(client):
    # first, create a test user to test the login later
    client.post('/signup', data={
        'username': "loginuser",
        'email': "loginuser@example.com",
        'password': "123456"
    })

    # test the login with the user info above
    response = client.post('/login', data={
        "email": "loginuser@example.com",
        "password": "123456"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Welcome" in response.data

#---------------------------------
# TEST LOGIN FAILURE
#---------------------------------
def test_login_failure(client):
    response = client.post('/login', data={
        "email": "login@example.com",
        "password": "wrong123"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Invalid email or password" in response.data

#---------------------------------
# TEST SIGNUP
#---------------------------------
def test_signup(client):
    response = client.post('/signup', data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "123456"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Account created successfully!" in response.data