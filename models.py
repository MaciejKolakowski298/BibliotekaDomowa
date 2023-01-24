import json


class Biblioteka:
    def __init__(self):
        try:
            with open("biblioteka.json", "r") as f:
                self.biblioteka = json.load(f)
        except FileNotFoundError:
            self.biblioteka = []

    def all(self):
        print(self.biblioteka)
        return self.biblioteka

    def get(self, id):
        return self.biblioteka[id]

    def create(self, data):
        data.pop('csrf_token')
        self.biblioteka.append(data)

    def save_all(self):
        with open("biblioteka.json", "w") as f:
            json.dump(self.biblioteka, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.biblioteka[id] = data
        self.save_all()


biblioteka = Biblioteka()