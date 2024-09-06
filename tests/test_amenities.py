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

# Test amenity creation API
def test_create_amenity(client):
    amenity_data = {
        'name': 'Pool',
        'description': 'A large outdoor swimming pool'
    }
    response = client.post('/api/v1/amenities/', data=json.dumps(amenity_data), content_type='application/json')
    assert response.status_code == 201
    assert response.json['message'] == 'Amenity created successfully'

# Test getting all amenities
def test_get_amenities(client):
    response = client.get('/api/v1/amenities/')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) > 0  # Assuming at least one amenity was created

# Test getting an amenity by ID
def test_get_amenity_by_id(client):
    response = client.get('/api/v1/amenities/')
    amenity_id = response.json[0]['id']

    response = client.get(f'/api/v1/amenities/{amenity_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Pool'

# Test updating an amenity
def test_update_amenity(client):
    response = client.get('/api/v1/amenities/')
    amenity_id = response.json[0]['id']

    updated_amenity_data = {
        'name': 'Heated Pool',
        'description': 'A large outdoor heated swimming pool'
    }
    response = client.put(f'/api/v1/amenities/{amenity_id}', data=json.dumps(updated_amenity_data), content_type='application/json')
    assert response.status_code == 200
    assert response.json['message'] == 'Amenity updated successfully'
    
    # Verify the update
    response = client.get(f'/api/v1/amenities/{amenity_id}')
    assert response.status_code == 200
    assert response.json['name'] == 'Heated Pool'
    assert response.json['description'] == 'A large outdoor heated swimming pool'
