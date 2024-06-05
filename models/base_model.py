import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', datetime.now())

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__dict__:
                setattr(self, key, value)
        self.updated_at = datetime.now()
