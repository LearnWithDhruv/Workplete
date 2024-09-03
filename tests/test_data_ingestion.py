# tests/test_data_ingestion.py
import unittest
from src.data_ingestion import load_data

class TestDataIngestion(unittest.TestCase):
    def test_load_data_csv(self):
        data = load_data('data/sample_data.csv')
        self.assertFalse(data.empty)
    
    def test_load_data_json(self):
        data = load_data('data/sample_data.json')
        self.assertFalse(data.empty)
    
    def test_load_data_excel(self):
        data = load_data('data/sample_data.xlsx')
        self.assertFalse(data.empty)

if __name__ == '__main__':
    unittest.main()
