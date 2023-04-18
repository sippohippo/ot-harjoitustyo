import unittest
from entities.exercise import Exercise
from entities.regular_user import RegularUser
from datetime import date


class TestRegularUser(unittest.TestCase):
    def setUp(self):
        print("")

    def test_regular_user_attributes_work(self):

        test_user = RegularUser("Hippo", "salari123")

        self.assertEqual(
            (test_user.username, test_user.password), ("Hippo", "salari123"))
