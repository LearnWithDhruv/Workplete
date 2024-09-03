# tests/test_data_preprocessing.py
import unittest
from src.data_preprocessing import clean_data
import pandas as pd

class TestDataPreprocessing(unittest.TestCase):
    def test_clean_data(self):
        data = pd.DataFrame({
            'A': [1, 2, None, 4],
            'B': [None, 2, 3, 4]
        })
        cleaned_data = clean_data(data)
        self.assertEqual(cleaned_data.isnull().sum().sum(), 0)

if __name__ == '__main__':
    unittest.main()
