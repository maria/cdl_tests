"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import  unittest

from django.test import TestCase

from factories import UserFactory


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class TestUser(unittest.TestCase):

    def test_user_attributes(self):
        user = UserFactory()
        self.assertIsNotNone(user.firstname)

    def test_users_have_different_names(self):
        user_one = UserFactory()
        user_two = UserFactory()
        self.assertNotEqual(user_one.firstname + user_one.lastname,
                            user_two.firstname + user_two.lastname,
                            "We have users with the same name!")

    def test_user_password_has_max_length(self):
        user = UserFactory()
        self.assertLessEqual(len(user.password), 20)
