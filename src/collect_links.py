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

if os.path.exists("../outputs/all_links.json"):
    with open("../outputs/all_links.json", 'r') as f:
        all_links = json.load(f)
    print(f"Resuming — loaded {len(all_links)} existing links")
else:
    all_links = []
    print("Starting fresh")

all_links_set = set(all_links)

# ── Main loop ────────────────────────────────────────────────────────────────
for idx, SEARCH in enumerate(SEARCHES):
    url = f"https://www.google.com/maps/search/{SEARCH.replace(' ', '+')}?gl=us&hl=en"
    driver.get(url)
    print(f"\n [{idx+1}/{len(SEARCHES)}] {SEARCH}")

    try:
        panel = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="feed"]'))
        )
        print("  Panel found ")
        for i in range(15):
            driver.execute_script("arguments[0].scrollTop += 1500", panel)
            time.sleep(1.5)
    except:
        print("  Panel not found, skipping")

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    links = soup.find_all('a', href=lambda h: h and '/maps/place/' in h)

    new_this_search = 0
    for a in links:
        href = a.get('href')
        if not href:
            continue
        full_url = href if href.startswith('http') else 'https://www.google.com' + href
        if full_url not in all_links_set:
            all_links_set.add(full_url)
            all_links.append(full_url)
            new_this_search += 1

    print(f"  New: {new_this_search} | Total unique: {len(all_links)}")

    # ── Checkpoint every 35 cities (= every 140 searches) ───────────────────
    if (idx + 1) % (35 * len(search_terms)) == 0:
        with open('all_links.json', 'w') as f:
            json.dump(all_links, f)
        city_number = (idx + 1) // len(search_terms)
        print(f"\n Checkpoint at city {city_number} | {len(all_links)} links saved")
        print("Cooling down 90 seconds...")
        time.sleep(90)

# ── Final save ───────────────────────────────────────────────────────────────
with open('all_links.json', 'w') as f:
    json.dump(all_links, f)
print(f"\n Done! {len(all_links)} unique links saved to all_links.json")
