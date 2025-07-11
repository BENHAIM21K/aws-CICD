import unittest
from lambda_function import lambda_handler

class TestLambdaFunction(unittest.TestCase):
    def test_hello_world_response(self):
        result = lambda_handler({}, {})
        self.assertEqual(result["statusCode"], 200)
        self.assertIn("Hello World", result["body"])

if __name__ == '__main__':
    unittest.main()
