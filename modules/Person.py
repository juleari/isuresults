class Person:
    def __init__(self, person_link):
        self.bio = person_link.url
        self.name = person_link.name

    def __repr__(self):
        return self.name
