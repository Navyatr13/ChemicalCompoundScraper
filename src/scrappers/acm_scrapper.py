import requests
from lxml import html
import time

def scrape_acm(query, base_url="https://dl.acm.org/action/doSearch"):
    """
    Scrape ACM for DOIs based on a query and return results in a unified format.
    """
    url = f"{base_url}?AllField={query}&pageSize=100"
    print(f"Querying ACM with URL: {url}")
    response = requests.get(url)
    time.sleep(1)  # To avoid hitting the server too fast
    tree = html.fromstring(response.content)
    papers = tree.xpath('//*[@class="hlFld-Title"]/a')

    results = []
    for paper in papers:
        if '/doi/' in paper.attrib['href']:
            doi = paper.attrib['href'].split('/doi/')[1]
            results.append({
                "compound_name": query,
                "source": "ACM",
                "type": "DOI",
                "value": doi
            })
    return results

if __name__ == "__main__":
    query = "Anti-inflammatory effects of Aspirin"
    res = scrape_acm(query)
    print(res)
