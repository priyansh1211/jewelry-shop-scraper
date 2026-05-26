# jewelry-shop-scraper

A Python-based web scraper that extracts contact information for jewelry shops in major US cities that currently do not have an active website. 

This tool is designed for B2B lead generation, helping digital agencies and marketers find offline businesses that need website development services.

## 🛠️ Built With

* **Python 3**
* **Selenium** (for dynamic page navigation and automated browser control)
* **BeautifulSoup4** (for fast, reliable HTML parsing)

## 🚀 Key Features

* **Targeted Search:** Scrapes major US metropolitan areas.
* **Lead Filtering:** Automatically filters out businesses that already have a website URL listed.
* **Data Export:** Saves leads (Name, Phone, Address, City) directly to a CSV file.

## 📋 Prerequisites

Before running the scraper, you need to install the required dependencies:

```bash
pip install selenium beautifulsoup4 pandas
```

*Note: Ensure you have the appropriate WebDriver installed (e.g., ChromeDriver for Google Chrome) matching your browser version.*

## 🧑‍💻 Usage

1. Clone the repository:
   ```bash
   git clone (https://github.com/priyansh1211/jewelry-shop-scraper)
   ```
2. Navigate into the directory:
   ```bash
   cd jewelry-shop-scraper
   ```
3. Run the script:
   ```bash
   python main.py
   ```

## ⚖️ Disclaimer

This project is for educational and research purposes only. Please use this tool responsibly and respect the Terms of Service of the platforms you are scraping.
