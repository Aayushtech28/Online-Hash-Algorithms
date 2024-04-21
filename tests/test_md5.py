import unittest
from src.hash_algorithms import md5

class TestMD5(unittest.TestCase):
    def test_md5_hash(self):
        # Test cases with known input-output pairs
        test_cases = [
            ("", "d41d8cd98f00b204e9800998ecf8427e"),
            ("hello", "5d41402abc4b2a76b9719d911017c592"),
            ("The quick brown fox jumps over the lazy dog", "9e107d9d372bb6826bd81d3542a419d6"),
            # Add more test cases as needed
        ]
        
        for input_data, expected_output in test_cases:
            with self.subTest(input_data=input_data):
                result = md5.md5_hash(input_data)
                self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()