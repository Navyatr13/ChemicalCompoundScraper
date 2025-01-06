from Bio import Entrez

# Always set the email for NCBI Entrez API
Entrez.email = "navyatr13@example.com"

def scrape_pubmed(query, max_results=100):
    """
    Search PubMed for articles matching the query.

    Parameters:
    - query (str): The search term or query.
    - max_results (int): Maximum number of results to retrieve (default is 100).

    Returns:
    - List of PubMed IDs (IdList) if successful, otherwise an empty list.
    """
    try:
        # Send a search request to PubMed
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        record = Entrez.read(handle)
        handle.close()  # Always close the handle
        return record.get("IdList", [])
    except Exception as e:
        print(f"An error occurred while querying PubMed: {e}")
    return []

if __name__ == "__main__":
    query = "Anti-inflammatory effects of Aspirin"
    pubmed_ids = scrape_pubmed(query)
    if pubmed_ids:
        print(f"PubMed IDs found for query '{query}':")
        print(pubmed_ids)
    else:
        print(f"No PubMed articles found for query '{query}'.")
