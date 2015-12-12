import re
import logging
import sys
import ConfigParser
from general import General
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import util
from authentication import AuthenticationProvider

# setting up logger
logger = util.setup_logger()
logger.info('Starting the bot')

config = ConfigParser.ConfigParser()
cfg = config.read('user.cfg')

username = ''
password = ''
universe = ''

if len(sys.argv) < 4 :
    if cfg == []:
        logger.info('You must pass 3 arguments (username, password, universe) or write have a config file')
        exit()
    else:
        logger.info('Getting user info from config file')
        username = config.get('UserInfo', 'username')
        password = config.get('UserInfo', 'password')
        universe = config.get('UserInfo', 'universe')
else:
    username = sys.argv[1]
    password = sys.argv[2]
    universe = sys.argv[3]

driver = AuthenticationProvider(username, password, universe).get_driver()
