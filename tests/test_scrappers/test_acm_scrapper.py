# test_acm_scrapper.py
from src.scrappers.acm_scraper import scrape_acm

def test_acm_scrapper():
    compound = "Aspirin"  # Example input
    results = scrape_acm(compound)
    print("ACM Scrapper Results:", results)

if __name__ == "__main__":
    test_acm_scrapper()
