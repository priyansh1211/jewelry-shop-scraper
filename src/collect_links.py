# Imports

import time
import os
import json

from bs4 import BeautifulSoup

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

with open("../config/cities.json") as f:
  city_names = json.load(f)

with open("../config/search_terms.json") as f:
  search_terms = json.load(f)

SEARCHES = [
    f"{term} in {city} USA"
    for city in city_names
    for term in search_terms
]
