from flask import request, jsonify
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.country import Country
from models.amenity import Amenity

def register_routes(app, storage):
    
    @app.route('/v1/users', methods=['POST'])
    def create_user_v1():
        data = request.json
        user = User(**data)
        storage.new(user)
        storage.save()
        return jsonify(user.__dict__), 201

    @app.route('/v1/places', methods=['POST'])
    def create_place_v1():
        data = request.json
        place = Place(**data)
        storage.new(place)
        storage.save()
        return jsonify(place.__dict__), 201

    @app.route('/v1/reviews', methods=['POST'])
    def create_review_v1():
        data = request.json
        review = Review(**data)
        storage.new(review)
        storage.save()
        return jsonify(review.__dict__), 201

    @app.route('/v1/cities', methods=['POST'])
    def create_city_v1():
        data = request.json
        city = City(**data)
        storage.new(city)
        storage.save()
        return jsonify(city.__dict__), 201

    @app.route('/v1/countries', methods=['POST'])
    def create_country_v1():
        data = request.json
        country = Country(**data)
        storage.new(country)
        storage.save()
        return jsonify(country.__dict__), 201

    @app.route('/v1/amenities', methods=['POST'])
    def create_amenity_v1():
        data = request.json
        amenity = Amenity(**data)
        storage.new(amenity)
        storage.save()
        return jsonify(amenity.__dict__), 201
