import lxml
from bs4 import BeautifulSoup
import re
import requests
import selenium

#constant links
CSP_LOGIN_PAGE = 'https://sims.rutgers.edu/csp/'

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")