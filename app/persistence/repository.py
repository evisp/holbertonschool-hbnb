from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        self._storage[obj.id] = obj
        print(f"Added object with ID: {obj.id}")  # Debug output
    
    def get(self, obj_id):
        obj = self._storage.get(obj_id)
        if obj:
            print(f"Retrieved object: {obj_id}")
        else:
            print(f"Object not found: {obj_id}")
        return obj

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj_id, data):
        if obj_id in self._storage:
            obj = self._storage[obj_id]
            # Update the attributes of the object based on the provided data
            for key, value in data.items():
                setattr(obj, key, value)
                print(f"Updated object with ID: {obj_id}")  # Debug output
        else:
            raise KeyError("Object not found")

    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]
            print(f"Deleted object with ID: {obj_id}")  # Debug output

    def get_by_attribute(self, attr_name, attr_value):
        obj = next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
        if obj:
            print(f"Found object with {attr_name}: {attr_value}")  # Debug output
        else:
            print(f"Object not found with {attr_name}: {attr_value}")  # Debug output
        return obj