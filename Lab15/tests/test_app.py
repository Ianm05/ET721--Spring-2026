"""
Ian Martinez
March 31, 2026
RestAPI's unit testing
"""

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        client.post('/reset')  # Clear store before every test
        yield client


# ----------------------------
# testing POST
# ----------------------------
def test_homepage(client):
    response = client.post('/items', json={'name': 'Book', 'Price': 10})

    assert response.status_code == 201
    data = response.get_json()

    assert 'id' in data
    assert data['item']['name'] == 'Book'
    assert data['item']['Price'] == 10


# ----------------------------
# testing GET
# ----------------------------
def test_get_single_item(client):
    client.post('/items', json={'name': 'Laptop', 'Price': 980})

    response = client.get('/items/1')

    assert response.status_code == 200
    assert response.get_json()['name'] == 'Laptop'


def test_get_all_items(client):
    client.post('/items', json={'name': 'Phone', 'Price': 130})
    client.post('/items', json={'name': 'Tablet', 'Price': 400})
    client.post('/items', json={'name': 'Watch', 'Price': 250})

    response = client.get('/items')

    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 3


# ----------------------------
# testing PUT (update)
# ----------------------------
def test_update_item(client):
    client.post('/items', json={'name': 'Phone', 'Price': 130})

    response = client.put('/items/1', json={'name': 'Tablet Pro', 'Price': 500})

    assert response.status_code == 200
    data = response.get_json()
    assert data['item']['name'] == 'Tablet Pro'


# ----------------------------
# testing DELETE
# ----------------------------
def test_delete_item(client):
    client.post('/items', json={'name': 'Book', 'Price': 10})

    response = client.delete('/items/1')

    assert response.status_code == 200
    get_all = client.get('/items')
    data = get_all.get_json()
    assert '1' not in data