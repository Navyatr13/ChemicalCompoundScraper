import unittest
from unittest.mock import patch
import requests

class TestScrapeChembl(unittest.TestCase):

    @patch("requests.get")
    def test_valid_response(self, mock_get):
        mock_response = {
            "molecules": [{"pref_name": "Aspirin", "molecule_chembl_id": "CHEMBL25"}]
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        from your_module import scrape_chembl  # Replace 'your_module' with the module name
        result = scrape_chembl("Aspirin")
        self.assertEqual(result, mock_response["molecules"])

    @patch("requests.get")
    def test_no_results(self, mock_get):
        mock_response = {}
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        from your_module import scrape_chembl
        result = scrape_chembl("NonexistentDrug")
        self.assertIsNone(result)

    @patch("requests.get")
    def test_request_exception(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        from your_module import scrape_chembl
        result = scrape_chembl("Aspirin")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
