

class Event:

    def __init__(self):
        pass

    def load_from_yaml_data(self, id, data):
        self.title = data.get('title')
        self.description = data.get('description')
        self.id = id