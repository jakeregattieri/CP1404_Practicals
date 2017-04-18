from Prac07.guitar import Guitar


class GuitarList:
    def __init__(self):
        self.guitars = []

    def __str__(self):
        return str([str(guitar) for guitar in self.guitars])

    def add(self, guitar):
        self.guitars.append(guitar)
