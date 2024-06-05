from models.base_model import BaseModel

class Country(BaseModel):
    def __init__(self, code, name, **kwargs):
        super().__init__(**kwargs)
        self.code = code
        self.name = name
