import urllib
from helper import ISU_EVENT_LINK
from IsuHTMLParser import IsuCatHTMLParser
from Person import Person

class ISUCategory:
    '''Lists of competitors and possible substitutes'''
    def __init__(self, name, entries):
        self.name = name
        self.entries = self.get_people([e for e in entries if e.has_number])
        self.substitutes = self.get_people([e for e in entries if not e.has_number])

    def get_people(self, entries):
        return map(Person, entries)

    def __repr__(self):
        return '%s - %s' % (self.name, str.join(', ', map(repr, self.entries)))

def get_category(link):
    """
    Returns category info.

    @param {Link} link
    @return {ISUCategory}
    """
    url = ISU_EVENT_LINK + link.url
    url_html = urllib.urlopen(url).read()

    parser = IsuCatHTMLParser()
    parser.feed(url_html)
    return ISUCategory(link.name, parser.a_list)
