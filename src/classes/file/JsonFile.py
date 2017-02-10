import json
import os

class JsonFile():

    def __init__(self, path):
        self.path = path

    def load(self):
        if os.path.isfile(self.path) == True:
            with open(self.path, "r") as fh:
                config = json.load(fh)
                return config
        else:
            return False

    def save(self, data):
        


    