from flask import Blueprint, request, jsonify
from models.user import User

# Create a Blueprint for user routes
user_routes = Blueprint('user_routes', __name__)

"""
# Endpoint for creating a new user
@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not all(key in data for key in ['email', 'first_name', 'last_name']):
        return jsonify({"error": "Missing required fields"}), 400
    
    # Validate email format
    if not is_valid_email(data['email']):
        return jsonify({"error": "Invalid email format"}), 400
    
    # Check if email is unique
    if User.find_by_email(data['email']):
        return jsonify({"error": "Email already exists"}), 409
    
    # Create the user
    user = User(**data)
    user.save()
    
    return jsonify(user.__dict__), 201
"""

# Endpoint for retrieving all users
@user_routes.route('/users', methods=['GET'])
def get_all_users():
    users = User.get_all()
    return jsonify([user.__dict__ for user in users]), 200

# Endpoint for retrieving a specific user by ID
@user_routes.route('/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user = User.find_by_id(user_id)
    if user:
        return jsonify(user.__dict__), 200
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint for updating a user by ID
@user_routes.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.find_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    # Update user fields
    for key, value in data.items():
        setattr(user, key, value)
    
    user.save()
    
    return jsonify(user.__dict__), 200

# Endpoint for deleting a user by ID
@user_routes.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.find_by_id(user_id)
    if user:
        user.delete()
        return jsonify({"message": "User deleted successfully"}), 204
    else:
        return jsonify({"error": "User not found"}), 404

# Helper function to validate email format
def is_valid_email(email):
    # Implement email validation logic here
    return True  # Placeholder implementation
