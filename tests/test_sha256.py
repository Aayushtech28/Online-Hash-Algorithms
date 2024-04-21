import unittest
from src.hash_algorithms import sha256

class TestSHA256(unittest.TestCase):
    def test_sha256_hash(self):
        # Test cases with known input-output pairs
        test_cases = [
            ("", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
            ("hello", "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"),
            ("The quick brown fox jumps over the lazy dog", "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592"),
            # Add more test cases as needed
        ]

        for input_data, expected_output in test_cases:
            with self.subTest(input_data=input_data):
                result = sha256.sha256_hash(input_data)
                self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()