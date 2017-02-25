import urllib
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter
from pdfminer.pdfpage import PDFPage
from IsuHTMLParser import IsuSheduleHTMLParser

class Shedule:
    '''Event shedule from pdf-link'''
    def __init__(self, url, parser):
        self.url = url
        self.local_practice = parser.local_practice
        self.local_competition = parser.local_competition

def get_fname(file_type):
    return 'document.%s' % file_type

def download_file(download_url):
    response = urllib.urlopen(download_url)
    pdf = open(get_fname('pdf'), 'w')
    pdf.write(response.read())
    pdf.close()

def get_shedule(url):
    """
    Gets shedule from pdf-link on event page
    @param {string} url
    @return {Shedule}
    """
    download_file(url)
    rsrcmgr = PDFResourceManager(caching=True)
    outpf = file(get_fname('html'), 'w')
    device = HTMLConverter(rsrcmgr, outfp, codec='utf-8', scale=1,
                           layoutmode='normal', laparams=LAParams(),
                           imagewriter=None)
    fp = file(get_fname('pdf'), 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(fp, pagenos, maxpages=0, password='',
                                  caching=True, check_extractable=True):
        interpreter.process_page(page)

    shedule_html = outpf.read()

    parser = IsuSheduleHTMLParser()
    parser.feed(shedule_html)

    fp.close()
    device.close()
    outfp.close()

    call('rm %s' % get_fname('pdf'), shell=True)
    call('rm %s' % get_fname('html'), shell=True)

    return Shedule(url, parser)
