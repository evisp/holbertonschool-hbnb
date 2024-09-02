import pytest
from app.models.amenity import Amenity

def test_amenity_creation():
    amenity = Amenity(name="Wi-Fi", description="High-speed internet")
    assert amenity.name == "Wi-Fi"
    assert amenity.description == "High-speed internet"

test_amenity_creation()

