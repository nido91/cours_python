import cours.introduction.boucles as e1
import unittest
import datetime

class TestLesson1(unittest.TestCase):

    def test_boucles(self):
        self.assertEqual(('Montlhéry', datetime.time(16, 30), 12800, 32.0, True), e1.exercice())

if __name__ == '__main__':
    unittest.main()