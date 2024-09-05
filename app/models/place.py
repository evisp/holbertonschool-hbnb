from app.models.base_model import BaseModel
from app.models.amenity import Amenity
from app.models.user import User
from app.models.review import Review


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id
        self.amenities = []
        self.reviews = []

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price must be a non-negative value")
        self._price = float(value)

    # Latitude validation: must be between -90 and 90
    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        if not (-90 <= value <= 90):
            raise ValueError("Latitude must be between -90 and 90")
        self._latitude = float(value)

    # Longitude validation: must be between -180 and 180
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        if not (-180 <= value <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        self._longitude = float(value)

    def add_amenity(self, amenity):
        """Add an amenity to the place"""
        if isinstance(amenity, Amenity) and amenity not in self.amenities:
            self.amenities.append(amenity)
        else:
            raise TypeError("amenity must be an instance of Amenity")

    def add_review(self, review):
        if isinstance(review, Review):
            self.reviews.append(review)
        else:
            raise TypeError("review must be an instance of Review")

    def remove_review(self, review):
        if review in self.reviews:
            self.reviews.remove(review)
        else:
            raise ValueError("Review not found in this place")

    def to_dict(self):
        """Override to_dict to include amenities and owner details"""
        place_dict = super().to_dict()
        place_dict.update({
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenities": [a.id for a in self.amenities],
            # Placeholder for owner details; this would be populated from the User model in the Facade
            "owner": {
                # Example of what might be included
                "id": self.owner_id,  # This would actually pull more detailed info via Facade
            }
        })
        return place_dict
