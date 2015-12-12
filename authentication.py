import logging
from bs4 import BeautifulSoup
import cookielib
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class AuthenticationProvider:

    def __init__(self, username, password, universe):
        self.login_url = 'http://br.ogame.gameforge.com/'
                        # http://s114-br.ogame.gameforge.com/game/index.php?page=overview
        self.index_url = 'http://s%s-br.ogame.gameforge.com' % universe + '/game/index.php'
        # headers = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
        # AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36')]
        # Dados de autenticacao
        self.username = username
        self.password = password
        self.universe = universe
        self.driver = webdriver.Firefox()
        self.logger = logging.getLogger('ogame-bot')


    def verify_connection(self):
        res = self.br.open(self.index_url)
        soup = BeautifulSoup(res.get_data())
        if soup.find("meta", { "name" : "ogame-player-name" }) == None:
            return False
        else:
            self.logger.info('Connection is ok')
            self.logger.info('Logged in as %s ' % soup.find("meta", { "name" : "ogame-player-name" })['content'])
            self.logger.info('Language is %s ' % soup.find("meta", { "name" : "ogame-language" })['content'])
            self.logger.info('Game version is %s ' % soup.find("meta", { "name" : "ogame-version" })['content'])
            return True

    def connect(self):
        # Open login page
        self.logger.info('Opening login page ' + self.login_url)
        self.driver.get(self.login_url)
        self.driver.find_element_by_id('loginBtn').click()
        Select(self.driver.find_element_by_id("serverLogin")).select_by_value("s%s-br.ogame.gameforge.com" % self.universe)
        self.driver.find_element_by_id('usernameLogin').send_keys(self.username)
        self.driver.find_element_by_id('passwordLogin').send_keys(self.password)
        self.driver.find_element_by_id('loginSubmit').click()
        self.logger.info('Logging in to server')

    def get_driver(self):
        self.connect()
        return self.driver
