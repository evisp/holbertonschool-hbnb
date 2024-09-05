import pytest
from flask import Flask
from flask_restx import Api
from flask_testing import TestCase
from app.api import api as places_api
from app.services.facade import HBnBFacade
from app.models.user import User
from app.models.place import Place

class TestPlaceEndpoints(TestCase):
    def create_app(self):
        app = Flask(__name__)
        api = Api(app, version='1.0', title='HBnB API', description='Test HBnB API')
        api.add_namespace(places_api, path='/api/v1/places')
        return app

    def setUp(self):
        self.facade = HBnBFacade()
        # Set up test data
        self.user = User(first_name="Alice", last_name="Smith", email="alice.smith@example.com", password="password123")
        self.facade.create_user(self.user.to_dict())
        self.place_data = {
            "title": "Cozy Apartment",
            "description": "A nice place to stay",
            "price": 100,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "owner_id": self.user.id
        }

    def test_create_place(self):
        response = self.client.post('/api/v1/places/', json=self.place_data)
        assert response.status_code == 201
        assert response.json['message'] == 'Place created successfully'
        assert 'id' in response.json

    def test_get_place(self):
        # Create a place
        response = self.client.post('/api/v1/places/', json=self.place_data)
        place_id = response.json['id']
        
        # Now get the place
        response = self.client.get(f'/api/v1/places/{place_id}')
        assert response.status_code == 200
        assert response.json['title'] == self.place_data['title']

    def test_update_place(self):
        # Create a place
        response = self.client.post('/api/v1/places/', json=self.place_data)
        place_id = response.json['id']
        
        # Update the place
        updated_data = {
            "title": "Updated Title",
            "description": "Updated Description",
            "price": 150
        }
        response = self.client.put(f'/api/v1/places/{place_id}', json=updated_data)
        assert response.status_code == 200