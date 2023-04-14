import unittest
import cap

class TestCap(unittest.TestCase):

    def test_one_word(self):
        actual = cap.cap_text("python")
        self.assertEqual("Python", actual)

    def test_mulitple_words(self):
        actual = cap.cap_text("monty python")
        self.assertEqual("Monty Python", actual)

if __name__ == '__main__':
    unittest.main()