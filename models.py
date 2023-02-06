import json


class Biblioteka:
    def __init__(self):
        try:
            with open("biblioteka.json", "r") as f:
                self.biblioteka = json.load(f)
        except FileNotFoundError:
            self.biblioteka = []

    def all(self):
        return self.biblioteka

    def get(self, id):
        return self.biblioteka[id - 1]

    def create(self, data):
        data.pop('csrf_token')
        self.biblioteka.append(data)

    def save_all(self):
        with open("biblioteka.json", "w") as f:
            json.dump(self.biblioteka, f)


    def update(self, id, data):
        data.pop('csrf_token')
        ksiazka = self.get(id)
        if ksiazka:
            index = self.biblioteka.index(ksiazka)
            self.biblioteka[index] = data
            self.save_all()
            return True
        return False
    
    def delete(self, id):
        ksiazka = self.get(id)
        if ksiazka:
            self.biblioteka.remove(ksiazka)
            self.save_all()
            return True
        return False



biblioteka = Biblioteka()