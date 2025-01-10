import logging
import requests

# Setup logging
logging.basicConfig(level=logging.INFO)

def fetch_url(url):
    """
    Fetch data from a given URL and handle errors.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        logging.error(f"Failed to fetch URL: {url}, Error: {e}")
        return None
