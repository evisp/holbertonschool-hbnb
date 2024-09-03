from app.models.base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

    def update(self, name=None, description=None):
        """Update the amenity's attributes"""
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    def to_dict(self):
        """Override to_dict to include description"""
        amenity_dict = super().to_dict()
        amenity_dict.update({
            "name": self.name,
            "description": self.description
        })
        return amenity_dict
