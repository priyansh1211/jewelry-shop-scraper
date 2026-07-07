# Known Limitations

This document outlines the current limitations of the Jewelry Shop Scraper and explains the reasoning behind several implementation decisions.

---

# 1. Google Maps HTML Structure

The scraper relies on the current HTML structure of Google Maps.

Since Google frequently updates its frontend, changes to HTML attributes or page layouts may require updates to the scraping logic.

---

# 2. Dynamic Content Loading

Google Maps loads business listings dynamically as the results panel is scrolled.

The scraper performs a fixed number of scrolls to balance completeness with execution time.

As a result:

- Some businesses may not be loaded.
- Extremely large cities may contain additional listings beyond the scrolling limit.

---

# 3. Rate Limiting

Large scraping sessions may trigger Google's anti-bot protections, including:

- CAPTCHA challenges
- Temporary request throttling
- Connection interruptions

To improve reliability, the scraper includes:

- Incremental checkpoint saving
- Resume support
- Periodic Chrome restarts
- Cooling periods between batches

These measures reduce failures but cannot completely eliminate detection.

---

# 4. Duplicate Businesses

The same business may appear under multiple search terms.

Example:

- Jewelry Shop
- Jeweler
- Jewelry Store
- Gold Shop

Duplicate listings are removed using the unique Google Maps URL.

---

# 5. Website Classification

The scraper identifies whether a business has an official website.

The following platforms are **not** considered official websites:

- Facebook
- Instagram
- WhatsApp
- X (Twitter)
- YouTube
- Yelp

Businesses using only these platforms are classified as not having an official website.

This behavior can be customized by modifying the list of excluded domains.

---

# 6. Phone Number Requirement

Businesses without a publicly listed phone number are skipped.

This is intentional because the primary objective is lead generation, where phone numbers are considered essential.

---

# 7. Geographic Filtering

The scraper currently keeps only businesses whose address contains:

```
United States
```

This prevents nearby international businesses from being included in the dataset.

---

# 8. Stale Activity Detection

Businesses with review activity older than the configured threshold are skipped.

The current implementation uses a heuristic based on review timestamps.

Although useful for reducing inactive businesses, it is not a definitive indicator that a business has permanently closed.

For this reason, the project includes a manual review workflow for validating a sample of skipped businesses.

---

# 9. Browser Automation

The scraper currently uses Selenium with Google Chrome.

Performance could be improved in future versions using:

- Playwright
- Browser contexts
- Parallel execution
- Headless mode

---

# 10. Long Running Sessions

Scraping thousands of businesses can require several hours depending on:

- Internet speed
- Google response times
- Number of search combinations

To reduce the impact of interruptions, the scraper periodically saves progress and can resume from previously generated checkpoint files.

---

# Future Improvements

Potential enhancements include:

- Proxy rotation
- Parallel scraping
- Playwright support
- Docker deployment
- Command-line interface
- Structured logging
- Retry strategies
- Unit tests
- Automatic CAPTCHA detection
- Configurable filtering rules

---

# Final Notes

This project was built as a portfolio demonstration of designing reliable, production-inspired web scraping workflows.

The focus was not only on extracting data, but also on creating a scraper that can recover from interruptions, minimize duplicate records, and generate clean, usable datasets.
