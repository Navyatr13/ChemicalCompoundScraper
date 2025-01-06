import sys
import os

# Explicitly add the `src` directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, ".."))
if src_dir not in sys.path:
    sys.path.append(src_dir)

from scrappers.chembl_scrapper import scrape_chembl
from scrappers.pubmed_scrapper import scrape_pubmed
from scrappers.acm_scrapper import scrape_acm
from semantic_search import semantic_search
from nlp_extraction import extract_entities
from database_manager import initialize_database, save_list, save_document

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

        # Scrape data using unified format
        acm_results = scrape_acm(compound) or []
        pubmed_results = scrape_pubmed(compound) or []
        chembl_results = scrape_chembl(compound) or []

        print(acm_results)
        print(pubmed_results)
        print(chembl_results)
        # Combine all results into a unified list
        unified_results = acm_results + pubmed_results + chembl_results
        # Save results to the database
        save_list(compound, unified_results)

    # Semantic search
    query = "Anti-inflammatory effects of Aspirin"
    search_results = semantic_search(query, documents)
    for content, score in search_results:
        save_document(compound_id=None, content=content, score=score)

    # NLP entity extraction
    for doc in documents:
        entities = extract_entities(doc)
        print(f"Extracted entities: {entities}")

    print("Pipeline complete!")

if __name__ == "__main__":
    main()
