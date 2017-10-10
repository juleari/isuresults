ID_NAME = 'FormView1_person_cnameLabel'

# mask for bio
BIO_MASK = 'http://www.isuresults.com/bios/isufs%s.htm'

# mask for personal bests
PB_MASK = 'http://www.isuresults.com/bios/isufs_pb_%s.htm'

# mask for competition results
CR_MASK = 'http://www.isuresults.com/bios/isufs_cr_%s.htm'

class Skater:
    '''
    Biography of skater
    @link_id {string} -- bio-link id at isuresults
    @name {string}
    @second_name {string}
    @country {code}
    @bests {Score}
    @results {[CompetitionResult]}
    '''
    def __init__(self, id):
        self.id = id
        self.url = BIO_MASK % id
        self.local_practice = parser.local_practice
        self.local_competition = parser.local_competition
