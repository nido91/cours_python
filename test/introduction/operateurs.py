import cours.introduction.operateurs as e2
import unittest


class TestLesson1(unittest.TestCase):

    def test_operateurs(self):
        self.assertEqual(('OK', 1), e2.exercice())

if __name__ == '__main__':
    unittest.main()