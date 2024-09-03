import unittest
from src.nlp_interface import parse_user_query

class TestNLPInterface(unittest.TestCase):
    def test_parse_user_query(self):
        self.assertEqual(parse_user_query("load data"), "LOAD_DATA")
        self.assertEqual(parse_user_query("clean data"), "CLEAN_DATA")
        self.assertEqual(parse_user_query("run analysis"), "RUN_ANALYSIS")
        self.assertEqual(parse_user_query("generate report"), "GENERATE_REPORT")
        self.assertEqual(parse_user_query("unknown command"), "UNKNOWN_COMMAND")

if __name__ == '__main__':
    unittest.main()
