import pytest
from app.models.user import User

def test_user_creation():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password123")
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.password == "password123"
    assert user.is_admin is False  # Default value

def test_user_update_profile():
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com", password="password123")
    user.update_profile(first_name="Jane", email="jane.doe@example.com")
    assert user.first_name == "Jane"
    assert user.email == "jane.doe@example.com"

def test_user_invalid_email():
    with pytest.raises(ValueError, match="Invalid email format"):
        user = User(first_name="John", last_name="Doe", email="invalid-email", password="password123")
        user.validate_email()

test_user_creation()

