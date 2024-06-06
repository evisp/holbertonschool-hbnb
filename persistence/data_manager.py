import json
import os
from persistence.ipersistence_manager import IPersistenceManager
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.country import Country
from models.amenity import Amenity

class DataManager(IPersistenceManager):
    __file_path = "file.json"
    __objects = {}
    __class_registry = {
        'User': User,
        'Place': Place,
        'Review': Review,
        'City': City,
        'Country': Country,
        'Amenity': Amenity
    }

    def save(self, entity):
        key = f"{entity.__class__.__name__}.{entity.id}"
        self.__objects[key] = entity
        self._save_to_file()

    def get(self, entity_id, entity_type):
        key = f"{entity_type}.{entity_id}"
        return self.__objects.get(key, None)

    def update(self, entity):
        key = f"{entity.__class__.__name__}.{entity.id}"
        if key in self.__objects:
            self.__objects[key] = entity
            self._save_to_file()

    def delete(self, entity_id, entity_type):
        key = f"{entity_type}.{entity_id}"
        if key in self.__objects:
            del self.__objects[key]
            self._save_to_file()

    def _save_to_file(self):
        json_objects = {key: obj.json() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
                for key, obj_dict in json_objects.items():
                    class_name = key.split('.')[0]
                    cls = self.__class_registry[class_name]
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj
