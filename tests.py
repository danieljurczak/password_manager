import os
import unittest

from database import DBConnection
from password import Password


class TestPassword(unittest.TestCase):

    def test_string_representation(self):
        new_password = Password(use_digits=False, use_special_characters=False)
        self.assertTrue(str(new_password).isalpha())

    def test_string_representation_with_digits(self):
        new_password = Password(use_special_characters=False)
        self.assertTrue(str(new_password).isalnum())

    def test_length(self):
        new_password = Password(length=10)
        self.assertEqual(len(new_password), 10)

    def test_string_length(self):
        new_password = Password(length=10)
        self.assertEqual(len(str(new_password)), 10)


class TestDBConnection(unittest.TestCase):
    def setUp(self) -> None:
        self.path = os.path.join(os.path.abspath(os.getcwd()), 'test_passwords.db')
        DBConnection.create_table(db_file=self.path)

    def tearDown(self) -> None:
        os.remove(self.path)

    def test_create_table(self):
        self.assertTrue(os.path.isfile(self.path))


if __name__ == '__main__':
    unittest.main()
