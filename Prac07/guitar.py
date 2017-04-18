class Guitar:
    CURRENT_DATE = 2017

    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{self.name} ({self.year}): ${self.cost:.2f}".format(self=self)

    def get_age(self):
        age = Guitar.CURRENT_DATE - self.year
        return age

    def is_vintage(self):
        vintage_string = ""
        if self.get_age() >= 50:
            vintage_string = "(Vintage!)"
        return vintage_string