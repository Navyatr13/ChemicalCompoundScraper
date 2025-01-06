from Bio import Entrez

# Always set the email for NCBI Entrez API
Entrez.email = "navyatr13@example.com"


def scrape_pubmed(query, max_results=100):
    """
    Search PubMed for articles matching the query and return results in a unified format.

    Parameters:
    - query (str): The search term or query.
    - max_results (int): Maximum number of results to retrieve (default is 100).

    Returns:
    - List of dictionaries with PubMed results in a unified format.
    """
    try:
        # Send a search request to PubMed
        handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
        record = Entrez.read(handle)
        handle.close()  # Always close the handle

        # Extract PubMed IDs
        pubmed_ids = record.get("IdList", [])

        # Convert to unified format
        results = [
            {
                "compound_name": query,
                "source": "PubMed",
                "type": "PubMed ID",
                "value": pubmed_id
            }
            for pubmed_id in pubmed_ids
        ]
        return results

    except Exception as e:
        print(f"An error occurred while querying PubMed: {e}")
        return []


if __name__ == "__main__":
    query = "Anti-inflammatory effects of Aspirin"
    pubmed_results = scrape_pubmed(query)
    if pubmed_results:
        print(f"PubMed results found for query '{query}':")
        print(pubmed_results)
    else:
        print(f"No PubMed articles found for query '{query}'.")
