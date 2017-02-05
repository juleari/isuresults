CATEGORY_ID = 'EventCategories'

class Link:
    '''Link on isuresults event page'''
    def __init__(self, attrs):
        for attr in attrs:
            if attr[0] == 'href':
                self.url = attr[1]
            elif attr[0] == 'id':
                self.id = 'cat' if CATEGORY_ID in attr[1] else 'url'

    def set_name(self, name):
        self.name = name

    def __repr__(self):
        return '%s - %s' % (self.name, self.url)

class PersonalLink(Link):
    '''Link to the event's person'''
    def __init__(self, attrs, has_number):
        self.has_number = has_number
        for attr in attrs:
            if attr[0] == 'href':
                self.url = attr[1]

    def __repr__(self):
        template = '%s - %s' if self.has_number else '(%s - %s)'
        return template % (self.name, self.url)
