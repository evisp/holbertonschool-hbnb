import pytest
import json
from app import create_app  # Assuming you have a function to create your Flask app
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

# Create a user to use as an owner in place tests
@pytest.fixture(scope='module')
def user_id(client):
    user_data = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'email': 'jane.doe@example.com',
        'password': 'password123',
        'is_admin': False
    }
    response = client.post('/api/v1/users/', data=json.dumps(user_data), content_type='application/json')
    return response.json['id']

# Test place creation API
def test_create_place(client, user_id):
    place_data = {
        'title': 'Cozy Cottage',
        'description': 'A small but cozy cottage in the countryside',
        'price': 75.0,
        'latitude': 37.7749,
        'longitude': -122.4194,
        'owner_id': user_id
    }
    response = client.post('/api/v1/places/', data=json.dumps(place_data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == 'Place created successfully'

# Test getting all places
def test_get_places(client):
    response = client.get('/api/v1/places/')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0  # Assuming at least one place was created

# Test getting a place by ID
def test_get_place_by_id(client, user_id):
    # First, create a place to retrieve
    place_data = {
        'title': 'Cozy Cottage',
        'description': 'A small but cozy cottage in the countryside',
        'price': 75.0,
        'latitude': 37.7749,
        'longitude': -122.4194,
        'owner_id': user_id
    }
    response = client.post('/api/v1/places/', data=json.dumps(place_data), content_type='application/json')
    place_id = response.json['id']

    response = client.get(f'/api/v1/places/{place_id}')
    assert response.status_code == 200
    assert response.json['title'] == 'Cozy Cottage'
    assert response.json['latitude'] == 37.7749
    assert response.json['longitude'] == -122.4194

# Test updating a place
def test_update_place(client, user_id):
    # First, create a place to update
    place_data = {
        'title': 'Cozy Cottage',
        'description': 'A small but cozy cottage in the countryside',
        'price': 75.0,
        'latitude': 37.7749,
        'longitude': -122.4194,
        'owner_id': user_id
    }
    response = client.post('/api/v1/places/', data=json.dumps(place_data), content_type='application/json')
    place_id = response.json['id']

    updated_place_data = {
        'title': 'Cozy Cottage Updated',
        'description': 'An updated description for the cozy cottage',
        'price': 85.0,
        'latitude': 37.7790,
        'longitude': -122.4195,
        'owner_id': user_id
    }
    response = client.put(f'/api/v1/places/{place_id}', data=json.dumps(updated_place_data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == 'Place updated successfully'
    
    # Verify the update
    response = client.get(f'/api/v1/places/{place_id}')
    assert response.status_code == 200
    assert response.json['title'] == 'Cozy Cottage Updated'
    assert response.json['description'] == 'An updated description for the cozy cottage'
    assert response.json['price'] == 85.0
    assert response.json['latitude'] == 37.7790
    assert response.json['longitude'] == -122.4195
