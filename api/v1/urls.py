from flask import request, jsonify
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.country import Country
from models.amenity import Amenity

def register_routes(app, data_manager):
    
    @app.route('/v1/users', methods=['POST'])
    def create_user_v1():
        data = request.json
        user = User(**data)
        data_manager.save(user)
        return jsonify(user.__dict__), 201

    @app.route('/v1/places', methods=['POST'])
    def create_place_v1():
        data = request.json
        place = Place(**data)
        data_manager.save(place)
        return jsonify(place.__dict__), 201

    @app.route('/v1/reviews', methods=['POST'])
    def create_review_v1():
        data = request.json
        review = Review(**data)
        data_manager.save(review)
        return jsonify(review.__dict__), 201

    @app.route('/v1/cities', methods=['POST'])
    def create_city_v1():
        data = request.json
        city = City(**data)
        data_manager.save(city)
        return jsonify(city.__dict__), 201

    @app.route('/v1/countries', methods=['POST'])
    def create_country_v1():
        data = request.json
        country = Country(**data)
        data_manager.save(country)
        return jsonify(country.__dict__), 201

    @app.route('/v1/amenities', methods=['POST'])
    def create_amenity_v1():
        data = request.json
        amenity = Amenity(**data)
        data_manager.save(amenity)
        return jsonify(amenity.__dict__), 201
