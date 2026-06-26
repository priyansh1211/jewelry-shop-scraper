import json
import os
import time

import pandas as pd
from tqdm import tqdm

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
  """
  Create and return a Chrome WebDriver instance.
  """
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service)

FAKE_WEBSITES = [
    'facebook.com', 'fb.com',
    'whatsapp.com', 'wa.me', 'chat.whatsapp.com',
    'instagram.com', 'twitter.com', 'x.com',
    'youtube.com', 'yelp.com'
]

def has_real_website(website):
    if not website:
        return False
    return not any(fake in website.lower() for fake in FAKE_WEBSITES)

def load_links():
  """
  Load Google Maps Business links.
  """
  with open("../config/all_links.json") as f:
    return json.load(f)

all_links = load_links()

def load_progress():
  
  
