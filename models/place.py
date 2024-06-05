from models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, host_id, name, description, number_of_rooms, number_of_bathrooms, max_guests, price_per_night, latitude, longitude, city_id, amenity_ids, **kwargs):
        super().__init__(**kwargs)
        self.host_id = host_id
        self.name = name
        self.description = description
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guests = max_guests
        self.price_per_night = price_per_night
        self.latitude = latitude
        self.longitude = longitude
        self.city_id = city_id
        self.amenity_ids = amenity_ids
