import sqlite3
from entities.character import Character


def init_db():
    conn = sqlite3.connect('character_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY, gender TEXT,
                   life_stage TEXT, voice TEXT, aspiration TEXT, skin_tone TEXT,
                   hair_style TEXT, hair_color TEXT, eye_color TEXT)''')
    conn.commit()
    conn.close()


def save_character(character):
    conn = sqlite3.connect('character_data.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO characters (gender, life_stage, voice, aspiration,
                   skin_tone, hair_style, hair_color, eye_color) 
        VALUES (:Gender, :Life_Stage, :Voice, :Aspiration,
                   :Skin_Tone, :Hair_Style, :Hair_Color, :Eye_Color)
    ''', (character.gender, character.life_stage, character.voice, character.aspiration,
          character.skin_tone, character.hair_style, character.hair_color, character.eye_color))
    conn.commit()
    conn.close()


def get_characters():
    conn = sqlite3.connect('character_data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM characters''')
    characters_data = cursor.fetchall()
    conn.close()

    characters = []
    for data in characters_data:
        character = Character(*data)
        characters.append(character)
    return characters
