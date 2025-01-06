import requests
import xml.etree.ElementTree as ET

def scrape_chembl(drug_name):
    """
    Query ChEMBL for drug synonyms using the synonyms endpoint.
    Parse the XML response to extract synonyms.
    """
    base_url = "https://www.ebi.ac.uk/chembl/api/data/molecule?molecule_synonyms?"
    params = {"synonym": drug_name}
    headers = {"User-Agent": "ChemicalCompoundScraper/1.0"}

    try:
        print(f"Querying ChEMBL for synonym: {drug_name}")
        response = requests.get(base_url, params=params, headers=headers, timeout=10)
        print(f"URL: {response.url}")  # Debugging the constructed URL
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the XML response
        root = ET.fromstring(response.content)

        # Extract all synonyms
        synonyms = []
        for synonym in root.findall(".//synonyms"):
            synonyms.append(synonym.text)

        if synonyms:
            return synonyms
        else:
            print(f"No synonyms found for {drug_name}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while querying ChEMBL: {e}")
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")

    return None

if __name__ == "__main__":
    query = "Asprin"
    res = scrape_chembl(query)
    if res:
        print("Synonyms found:")
        print(res)
    else:
        print("No data returned from ChEMBL.")
