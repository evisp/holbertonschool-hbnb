import json
import os

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        json_objects = {}
        for key, obj in FileStorage.__objects.items():
            json_objects[key] = obj.__dict__
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                json_objects = json.load(f)
                for key, obj_dict in json_objects.items():
                    class_name = key.split('.')[0]
                    cls = globals()[class_name]
                    obj = cls(**obj_dict)
                    FileStorage.__objects[key] = obj
