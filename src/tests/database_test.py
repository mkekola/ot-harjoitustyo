import unittest
import sqlite3
from entities.character import Character
from database import init_db, register_user, login_user, save_character, get_characters


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(':memory:')
        init_db(self.connection)

    def tearDown(self):
        self.connection.close()

    def test_register_user_successful(self):
        result = register_user("newuser", "password123", self.connection)
        self.assertTrue(result)

    def test_register_user_failure(self):
        register_user("newuser", "password123", self.connection)
        result = register_user("newuser", "password123", self.connection)  # Try to register the same user again
        self.assertFalse(result)

    def test_login_user_successful(self):
        register_user("newuser", "password123", self.connection)
        result = login_user("newuser", "password123", self.connection)
        self.assertTrue(result)
    
    def test_login_user_failure(self):
        result = login_user("newuser", "password123", self.connection)
        self.assertFalse(result)


