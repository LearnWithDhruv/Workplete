import unittest
from src.analysis_engine import run_analysis
import pandas as pd

class TestAnalysisEngine(unittest.TestCase):
    def test_run_analysis(self):
        data = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [1, 2, 3, 4]
        })
        results = run_analysis(data)
        self.assertEqual(len(results), 3)

if __name__ == '__main__':
    unittest.main()
