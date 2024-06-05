import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', str(datetime.now()))
        self.updated_at = kwargs.get('updated_at', str(datetime.now()))

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__dict__:
                setattr(self, key, value)
        self.updated_at = str(datetime.now())

    def json(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

