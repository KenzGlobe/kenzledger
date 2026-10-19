# Imports
import unittest
import os
import json
from storage import load_transactions as load_tx, save_transactions as save_tx

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_data.json"
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    # --- TEST 1 ---
    def test_save_and_load(self):
        dummy_data = [
            {"type": "expense", "amount": 500, "category": "food", "description": "lunch"}
        ]
        save_tx(dummy_data, self.test_filename)
        loaded_data = load_tx(self.test_filename)
        self.assertEqual(dummy_data, loaded_data)

    # --- TEST 2 ---
    def test_load_missing_file(self):
        result = load_tx("this_file_does_not_exist.json")
        self.assertEqual(result, [])

    # --- TEST 3 ---
    def test_load_corrupt_file(self):
        with open(self.test_filename, "w") as file:
            file.write("This is not JSON!")
            
        result = load_tx(self.test_filename)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()

