import unittest
from app.main import say_hello

class TestMain(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, Jenkins!")

if __name__ == "__main__":
    unittest.main()