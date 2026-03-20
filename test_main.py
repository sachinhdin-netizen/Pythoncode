import unittest
from main import add

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 5), 10)

if __name__ == "__main__":
    unittest.main()
