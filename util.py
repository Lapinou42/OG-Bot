import mechanize
import logging

class UrlProvider:
    def __init__(self, universe):
        self.main_url = 'http://s' + str(universe) + '-br.ogame.gameforge.com/game/index.php'

        self.pages = {
            'main':         self.main_url + '?page=overview',
            'resources':    self.main_url + '?page=resources',
            'station':      self.main_url + '?page=station',
            'research':     self.main_url + '?page=research',
            'shipyard':     self.main_url + '?page=shipyard',
            'defense':      self.main_url + '?page=defense',
            'fleet':        self.main_url + '?page=fleet1',
            'galaxy':       self.main_url + '?page=galaxy',
            'galaxyCnt':    self.main_url + '?page=galaxyContent',
            'events':       self.main_url + '?page=eventList'
        }

    def get_pages(self):
        """
        Returns list of pages
        """
        return self.pages

    def get_page_url(self, page, planet = None):
        """
        Get page url for planet
        """
        url = self.pages.get(page)
        if planet is not None:
            url += '&cp=%s' % planet[1]
        return url

    def get_main_url(self):
        """
        Return the main url
        """
        return self.main_url

def sanitize(t):
    for i in t:
        try:
            yield int(i)
        except ValueError:
            yield i

def submit_request(browser):
    for attempt in (1, 3):
        try:
            res = browser.submit()
            return res
        except mechanize.URLError:
            self.error("URLError submitting form, trying again for the %sth time" % attempt)

def setup_logger():
    logger = logging.getLogger('ogame-bot')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
