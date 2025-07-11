import unittest
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_lambda_response_structure(self):
        result = lambda_handler({}, {})

        # Check that 'statusCode' exists and is 200
        self.assertIn("statusCode", result)
        self.assertEqual(result["statusCode"], 200)

        # Check that 'body' exists and is a non-empty string
        self.assertIn("body", result)
        self.assertIsInstance(result["body"], str)
        self.assertTrue(len(result["body"]) > 0)

if __name__ == '__main__':
    unittest.main()
