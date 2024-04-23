import unittest
from entities.character import Character


class TestCharacter(unittest.TestCase):
    def test_init_random(self):
        char = Character()
        self.assertIn(char.gender, Character.genders)
        self.assertIn(char.life_stage, Character.life_stages)
        self.assertIn(char.voice, Character.voices)
        self.assertIn(char.aspiration, Character.aspirations)
        self.assertIn(char.skin_tone, Character.skin_tones)
        self.assertIn(char.hair_style, Character.hair_styles)
        self.assertIn(char.hair_color, Character.hair_colors)
        self.assertIn(char.eye_color, Character.eye_colors)

    def test_init_specific(self):
        char = Character(gender="Female", life_stage="Adult", voice="Warm", aspiration="Love",
                         skin_tone="Warm Light", hair_style="Long", hair_color="Black", eye_color="Blue")
        self.assertEqual(char.gender, "Female")
        self.assertEqual(char.life_stage, "Adult")
        self.assertEqual(char.voice, "Warm")
        self.assertEqual(char.aspiration, "Love")
        self.assertEqual(char.skin_tone, "Warm Light")
        self.assertEqual(char.hair_style, "Long")
        self.assertEqual(char.hair_color, "Black")
        self.assertEqual(char.eye_color, "Blue")
