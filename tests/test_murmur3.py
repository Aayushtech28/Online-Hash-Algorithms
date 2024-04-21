import unittest
from src.hash_algorithms import murmur3

class TestMurmurHash3(unittest.TestCase):
    def test_murmur3_hash(self):
        # Test cases with known input-output pairs
        test_cases = [
            ("", 0),
            ("hello", 907865676),
            ("The quick brown fox jumps over the lazy dog", 1949770507),
            # Add more test cases as needed
        ]
        
        for input_data, expected_output in test_cases:
            with self.subTest(input_data=input_data):
                result = murmur3.murmur3_hash(input_data)
                self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()