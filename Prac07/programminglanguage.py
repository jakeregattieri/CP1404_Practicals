

class ProgrammingLanguage:
    def __init__(self, name='', typing='', reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{self.name}, {self.typing} typing, Reflection={self.reflection}, first appeared in {self.year}".format(self=self)

    def is_dynamic(self):
        return self.reflection
