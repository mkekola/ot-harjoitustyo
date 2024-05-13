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
        result = register_user("newuser", "password123", self.connection)
        self.assertFalse(result)

    def test_login_user_successful(self):
        register_user("newuser", "password123", self.connection)
        result = login_user("newuser", "password123", self.connection)
        self.assertTrue(result)

    def test_login_user_failure(self):
        result = login_user("newuser", "password123", self.connection)
        self.assertFalse(result)

    def test_empty_character_list(self):
        characters = get_characters(1, self.connection)
        self.assertEqual(characters, [])

    def test_save_character(self):
        character = Character()
        save_character(character, 1, self.connection)
        characters = get_characters(1, self.connection)
        self.assertEqual(len(characters), 1)
