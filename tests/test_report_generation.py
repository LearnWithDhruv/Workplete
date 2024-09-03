# tests/test_report_generation.py
import unittest
from src.report_generation import generate_report
import pandas as pd

class TestReportGeneration(unittest.TestCase):
    def test_generate_report(self):
        data = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [1, 2, 3, 4]
        })
        results = ([1, 2, 3, 4], [0, 1, 0, 1], [1, 1, 1, 1])
        generate_report(data, results)
        self.assertTrue(True)  # Test to ensure the report generation runs without errors

if __name__ == '__main__':
    unittest.main()
