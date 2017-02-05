from HTMLParser import HTMLParser
from Link import Link, PersonalLink

NAME_ID = 'FormView1_event_nameLabel'
CITY_ID = 'FormView1_event_cityLabel'
NATI_ID = 'FormView1_event_nationLabel'

START_ID = 'FormView1_event_start_dateLabel'
END_ID = 'FormView1_event_end_dateLabel'

class IsuHTMLParser(HTMLParser):
    """HTMLParser for isuresults event page"""
    def __init__(self):
        self.clear_tag()
        HTMLParser.__init__(self)

    def parse_a(self, attrs):
        self.tag = 'a'
        self.elem = Link(attrs)

    def parse_span(self, attrs):
        self.tag = 'span'
        for attr in attrs:
            if attr[0] == 'id':
                self.id = attr[1]

    def clear_tag(self):
        self.tag = None
        self.elem = None
        self.id = None

    def set_name(self, name):
        self.name = name
    def set_city(self, city):
        self.city = city
    def set_nati(self, nati):
        self.nati = nati
    def set_start(self, start):
        self.start = start
    def set_end(self, end):
        self.end = end

    def handle_starttag(self, tag, attrs):
        {
            'a'   : lambda x: self.parse_a(x),
            'span': lambda x: self.parse_span(x),

        }.get(tag, lambda x: self.clear_tag())(attrs)

    def handle_data(self, data):
        if self.tag == 'a':
            self.elem.set_name(data)
        if self.tag == 'span':
            {
                NAME_ID: lambda x: self.set_name(x),
                CITY_ID: lambda x: self.set_city(x),
                NATI_ID: lambda x: self.set_nati(x),

                START_ID: lambda x: self.set_start(x),
                END_ID  : lambda x: self.set_end(x)

            }.get(self.id, lambda x: self.clear_tag())(data)

            self.clear_tag()

    def handle_endtag(self, tag):
        if tag == 'a':
            try:
                self.a_list.append(self.elem)
            except AttributeError:
                self.a_list = [self.elem]

        self.clear_tag()

class IsuCatHTMLParser(IsuHTMLParser):
    """HTMLParser for isuresults category page"""
    def parse_a(self, attrs):
        self.tag = 'a'
        self.elem = PersonalLink(attrs, self.has_number)

    def parse_td(self, attrs):
        for attr in attrs:
            if attr[0] == 'class' and attr[1] == 'first':
                self.tag = 'td_first'

    def clear_tag(self):
        IsuHTMLParser.clear_tag(self)
        self.has_number = False

    def handle_starttag(self, tag, attrs):
        {
            'a' : lambda x: self.parse_a(x),
            'td': lambda x: self.parse_td(x),

        }.get(tag, lambda x: self.clear_tag())(attrs)

    def handle_data(self, data):
        if self.tag == 'a':
            self.elem.set_name(data)
        elif self.tag == 'td_first':
            self.has_number = True
        else:
            self.clear_tag()

    def handle_endtag(self, tag):
        if tag == 'a':
            try:
                self.a_list.append(self.elem)
            except AttributeError:
                self.a_list = [self.elem]

        if self.tag != 'td_first':
            self.clear_tag()
