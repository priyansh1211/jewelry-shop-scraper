# 💎 Jewelry Shop Scraper

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.x-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A production-style Google Maps scraper built with Python, Selenium, and BeautifulSoup to discover jewelry businesses across the United States, extract business information, filter qualified leads, and export clean datasets for sales prospecting and lead generation.

---

## Project Overview

Finding qualified local business leads manually is time-consuming and difficult to scale.

This project automates the process of searching Google Maps across hundreds of U.S. cities, collecting jewelry business listings, extracting business information, filtering businesses that already have an official website, and exporting structured datasets ready for outreach or further analysis.

The scraper was designed with reliability in mind and includes features such as checkpointing, crash recovery, duplicate removal, configurable search parameters, and incremental data saving for long-running scraping sessions.

---

## Features

- Search jewelry businesses across **385+ U.S. cities**
- Multiple search keywords per city for broader coverage
- Automatic duplicate removal
- Resume interrupted scraping sessions
- Automatic checkpoint saving
- Chrome restart mechanism to reduce memory issues
- Skip permanently closed businesses
- Skip businesses without phone numbers
- Skip non-U.S. businesses
- Filter businesses that already have official websites
- Clean and normalize scraped data
- Export results as CSV and Excel
- Manual review workflow for stale listings
- Configurable cities and search terms

---

## Repository Structure

```text
jewelry-shop-scraper/
│
├── config/
│   ├── cities.json
│   └── search_terms.json
│
├── data/
│   ├── README.md
│   └── sample/
│       ├── jewelry_all_sample.csv
│       └── jewelry_final_sample.csv
│
├── docs/
│   ├── diagrams/
│   └── screenshots/
│
├── notebooks/
│   └── google_maps_jewelry_scraper.ipynb
│
├── src/
│   ├── collect_links.py
│   ├── scrape_business.py
│   └── utils.py
│
├── .gitignore
├── known_limitations.md
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Selenium | Browser automation |
| BeautifulSoup | HTML parsing |
| Pandas | Data processing |
| OpenPyXL | Excel export |
| WebDriver Manager | Automatic ChromeDriver management |
| tqdm | Progress tracking |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/priyansh1211/jewelry-shop-scraper.git

cd jewelry-shop-scraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

The scraper has been designed to be configurable without modifying the source code.

### Cities

Edit:

```
config/cities.json
```

to specify the list of cities to search.

Example:

```json
[
    "Houston",
    "Dallas",
    "Chicago"
]
```

### Search Terms

Edit:

```
config/search_terms.json
```

Example:

```json
[
    "jewelry shop",
    "jeweler",
    "jewelry store",
    "gold shop"
]
```

The scraper automatically generates search combinations using every city and every search term.

---

## Workflow

The project follows the workflow below:

1. Load configuration files.
2. Generate Google Maps search queries.
3. Search Google Maps for every city and keyword combination.
4. Collect unique business listing URLs.
5. Resume from previous checkpoints if available.
6. Visit every business listing.
7. Extract:
   - Business name
   - Phone number
   - Address
   - Website
8. Filter:
   - Permanently closed businesses
   - Non-U.S. businesses
   - Businesses without phone numbers
   - Businesses with stale activity
9. Identify businesses without official websites.
10. Export clean datasets to CSV and Excel.

---

## Output Files

The scraper generates several output files during execution.

| File | Description |
|------|-------------|
| jewelry_all.csv | All scraped businesses |
| jewelry_all.xlsx | Excel version of all businesses |
| jewelry_final.csv | Businesses without official websites |
| jewelry_final.xlsx | Excel version of filtered businesses |
| jewelry_progress.csv | Checkpoint for resume support |
| jewelry_skipped.csv | Businesses skipped during scraping |
| all_links.json | Cached Google Maps listing URLs |

---

## Sample Data

Example output files are available under:

```
data/sample/
```

These sample datasets demonstrate the format of the generated files without requiring users to execute the scraper.

---

## Engineering Decisions

Several design choices were made to improve reliability during long scraping sessions.

### Resume Support

The scraper automatically resumes from previously saved progress after interruptions.

### Checkpoint Saving

Progress is periodically saved to minimize data loss.

### Chrome Restart

Chrome is restarted after processing a configurable number of listings to reduce memory usage.

### Duplicate Removal

Businesses discovered through multiple search keywords are automatically deduplicated using their Google Maps URL.

### Website Classification

Businesses are classified based on whether they have an official website. Links to common social platforms such as Facebook, Instagram, WhatsApp, X (Twitter), and YouTube are not considered official business websites.

---

## Known Limitations

This scraper depends on the current structure of Google Maps.

Possible limitations include:

- Google Maps HTML structure may change over time.
- Large scraping sessions may trigger rate limiting or CAPTCHA challenges.
- Some businesses intentionally do not publish phone numbers.
- Infinite scrolling means not every business is guaranteed to be loaded.
- Businesses using only social media pages are treated as not having an official website.

Additional details are available in **known_limitations.md**.

---

## Future Improvements

Potential enhancements include:

- Playwright implementation
- Headless execution mode
- Proxy rotation
- Parallel scraping
- Docker support
- Command-line interface
- Logging framework
- Unit testing
- Retry strategies
- Automatic CAPTCHA detection

---

## Disclaimer

This project was created for educational and portfolio purposes.

Users are responsible for ensuring that their use of this project complies with Google Maps Terms of Service and all applicable laws and regulations.

---

## Author

**Priyansh Bhatt**

This project is part of my Python Web Scraping portfolio and demonstrates building reliable, production-inspired data collection pipelines using Selenium, BeautifulSoup, and Pandas.

If you found this repository useful, consider giving it a ⭐.
