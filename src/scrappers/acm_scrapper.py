import requests
from lxml import html
import time

def scrape_acm(query, base_url="https://dl.acm.org/action/doSearch"):
    """
    Scrape ACM for DOIs based on a query.
    """
    url = f"{base_url}?AllField={query}&pageSize=100"
    print(url)
    response = requests.get(url)
    time.sleep(1)
    tree = html.fromstring(response.content)
    papers = tree.xpath('//*[@class="hlFld-Title"]/a')
    return [paper.attrib['href'].split('/doi/')[1] for paper in papers if '/doi/' in paper.attrib['href']]

if __name__ == "__main__":
    query = "Anti-inflammatory effects of Aspirin"
    res = scrape_acm(query)
    print(res)
