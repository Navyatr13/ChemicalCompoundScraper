import sys
import os
# Explicitly add the `src` directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, ".."))

#from src.scrappers.acm_scraper import scrape_acm
from scrappers.chembl_scrapper import scrape_chembl
from scrappers.pubmed_scrapper import scrape_pubmed
from scrappers.acm_scrapper import scrape_acm
from semantic_search import semantic_search
from nlp_extraction import extract_entities
from database_manager import initialize_database, save_compound, save_document

def main():
    # Initialize database
    initialize_database()

    # Input data
    compounds = ["Aspirin", "Ibuprofen"]
    documents = [
        "Aspirin inhibits COX1 and COX2.",
        "Ibuprofen reduces inflammation via prostaglandins.",
        "Paracetamol affects pain relief mechanisms."
    ]

    # Scraping
    for compound in compounds:
        print(f"Scraping data for: {compound}")
        acm_results = scrape_acm(compound)
        pubmed_results = scrape_pubmed(compound)
        chembl_results = scrape_chembl(compound)
        print( acm_results, pubmed_results, chembl_results )
        # Save results
        save_compound(compound, acm_results, pubmed_results, chembl_results)

    # Semantic search
    query = "Anti-inflammatory effects of Aspirin"
    search_results = semantic_search(query, documents)
    save_document(search_results)

    # NLP entity extraction
    for doc in documents:
        entities = extract_entities(doc)
        print(f"Extracted entities: {entities}")

    print("Pipeline complete!")

if __name__ == "__main__":
    main()
