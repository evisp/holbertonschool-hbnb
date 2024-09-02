from app.models.base_model import BaseModel
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

    def add_amenity(self, amenity):
        """Add an amenity to the place"""
        if amenity not in self.amenities:
            self.amenities.append(amenity)

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
        """Override to_dict to include amenities"""
        place_dict = super().to_dict()
        place_dict.update({
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "owner_id": self.owner_id,
            "amenities": [a.id for a in self.amenities]
        })
        return place_dict
