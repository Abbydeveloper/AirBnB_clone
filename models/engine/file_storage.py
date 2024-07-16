#!/usr/bin/python3
"""File Storage module"""
import json


class FileStorage():
    """FileStorage class serializes instances to a JSON file and deserializes
    JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""

        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""

        objects = FileStorage.__objects
        obj_dict = {obj: objects[obj].to_dict() for obj in objects.keys()}
        with open(FileStorage.__file_path, mode="w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise do nothing. If the file doesn't
        exist, no exception should be raised"""

        try:
            with open(FileStorage.__file_path) as f:
                objects = json.load(f)
                for obj in objects.values():
                    cls = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls)(**obj))
        except FileNotFoundError:
            return
