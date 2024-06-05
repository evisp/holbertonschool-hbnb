from models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
