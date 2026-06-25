# Jewelry Business Lead Generation System

A Python-based lead generation tool that discovers jewelry businesses across the United States and identifies stores that do not have a dedicated website.

The scraper automates Google Maps data collection, extracts business contact information, filters businesses that already have a website, and generates a list of qualified leads for digital marketing agencies, website development firms, SEO consultants, and sales teams.

---

## Business Problem

Many small jewelry businesses rely solely on Google Maps, Facebook, or Instagram for their online presence and do not have a dedicated website.

Finding these businesses manually is time-consuming and inefficient.

This project automates the process by:

* Discovering jewelry businesses from Google Maps
* Extracting contact information
* Identifying businesses without a dedicated website
* Generating qualified outreach leads

---

## Features

### Business Discovery

* Searches hundreds of US cities
* Supports multiple search keywords
* Collects Google Maps business listings

### Contact Extraction

* Business Name
* Phone Number
* Address
* Website
* Google Maps URL

### Lead Qualification

* Detects whether a business has a dedicated website
* Filters social media pages and directory listings
* Generates lists of businesses that may benefit from website development services

### Reliability Features

* Duplicate removal
* Progress checkpoints
* Resume after interruption
* Incremental CSV exports

---

## Technologies Used

* Python 3
* Selenium
* BeautifulSoup4
* Pandas
* NumPy
* WebDriver Manager
* JSON

---

## Project Structure

```text
jewelry-shop-scraper/

├── config/
├── data/
├── notebooks/
├── outputs/
├── screenshots/
├── src/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Workflow

```text
Google Maps Search
        ↓
Collect Business URLs
        ↓
Visit Business Pages
        ↓
Extract Contact Information
        ↓
Identify Website Status
        ↓
Generate Qualified Leads
        ↓
Export CSV Files
```

---

## Sample Output

| Business Name   | Phone        | Address    | Website | Website Available |
| --------------- | ------------ | ---------- | ------- | ----------------- |
| Example Jewelry | 123-456-7890 | Dallas, TX | None    | False             |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/priyansh1211/jewelry-shop-scraper.git
```

Move into the project directory:

```bash
cd jewelry-shop-scraper
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1 - Collect Google Maps URLs

```bash
python src/collect_links.py
```

### Step 2 - Scrape Business Information

```bash
python src/scrape_businesses.py
```

### Step 3 - Generate Qualified Leads

```bash
python src/clean_data.py
```

---

## Output Files

### All Businesses

```text
outputs/jewelry_all.csv
```

Contains all scraped businesses.

### Qualified Leads

```text
outputs/qualified_leads.csv
```

Contains businesses without a dedicated website.

### Summary Statistics

```text
outputs/summary.json
```

Contains scraping statistics and lead counts.

---

## Use Cases

This project can be used by:

* Website Development Agencies
* SEO Agencies
* Digital Marketing Firms
* Sales Teams
* Lead Generation Specialists
* Market Research Analysts

---

## Future Improvements

* Playwright support
* Proxy rotation
* State-wise analytics
* Lead scoring system
* Automated email enrichment
* Dashboard reporting

---

## Disclaimer

This project is intended for educational, research, and business intelligence purposes only.

Users are responsible for complying with the Terms of Service of any platform they access and for following all applicable laws and regulations regarding data collection and usage.

---

## Author

Priyansh Bhatt

GitHub:
https://github.com/priyansh1211
