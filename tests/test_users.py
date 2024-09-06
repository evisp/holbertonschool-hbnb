import pytest
import json
from app import create_app  # Assuming you have a function to create your Flask app
from app.models.user import User
from app.services.facade import HBnBFacade

# Setup Flask test client
@pytest.fixture(scope='module')
def client():
    app = create_app()  # Create your Flask app
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            # Initialize the database or in-memory data store
            facade = HBnBFacade()
            yield client

# Test user creation API
def test_create_user(client):
    user_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'password': 'password123',
        'is_admin': False
    }
    response = client.post('/api/v1/users/', data=json.dumps(user_data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == 'User created successfully'

# Test getting all users
def test_get_users(client):
    response = client.get('/api/v1/users/')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) == 1

# Test getting a user by ID
def test_get_user_by_id(client):
    response = client.get('/api/v1/users/')
    user_id = response.json[0]['id']

    response = client.get(f'/api/v1/users/{user_id}')
    assert response.status_code == 200
    assert response.json['email'] == 'john.doe@example.com'

# Test updating a user
def test_update_user(client):
    response = client.get('/api/v1/users/')
    user_id = response.json[0]['id']

    updated_user_data = {
        'first_name': 'Johnathan',
        'last_name': 'Doe',
        'email': 'johnathan.doe@example.com',
        'password': 'newpassword123'
    }
    response = client.put(f'/api/v1/users/{user_id}', data=json.dumps(updated_user_data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == 'User updated successfully'
    
    # Verify the update
    response = client.get(f'/api/v1/users/{user_id}')
    assert response.status_code == 200
    assert response.json['email'] == 'johnathan.doe@example.com'
