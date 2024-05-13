import sqlite3
from entities.character import Character


def init_db(connection):
    ''' Initializes the database if it does not exist.
    Args: 
        connection: Database connection.
    '''
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, 
                   username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY, user_id INTEGER, gender TEXT,
                   life_stage TEXT, voice TEXT, aspiration TEXT, skin_tone TEXT,
                   hair_style TEXT, hair_color TEXT, eye_color TEXT, FOREIGN KEY (user_id) REFERENCES users(id))''')
    connection.commit()

def register_user(username, password, connection):
    ''' Registers a user in the database.
    Args:
        username: Username.
        password: Password.
        connection: Database connection.
    '''
    cursor = connection.cursor()
    try:
        cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
        connection.commit()
        print("User registered successfully!")
        return True
    except sqlite3.IntegrityError:
        print("Username already exists.")
        return False
    
def login_user(username, password, connection=None):
    ''' Kirjaa käyttäjän sisään.
    Args:
        username: Käyttäjänimi.
        password: Salasana.
    Returns:
        True, jos kirjautuminen onnistui, muuten False.
        '''
    conn = connection
    if conn is None:
        conn = sqlite3.connect('character_data.db')

    cursor = conn.cursor()
    cursor.execute('''SELECT id FROM users WHERE username = :Username AND password = :Password''',
                   (username, password))
    user = cursor.fetchone()
    conn.close()
    if user is not None:
        print("Login successful!")
        return user[0]
    else:
        print("Login failed.")
        return None

def save_character(character, user, connection=None):
    ''' Tallentaa hahmon tietokantaan.
    Args:
        character: Hahmo, joka tallennetaan tietokantaan.
        '''
    conn = connection
    if conn is None:
        conn = sqlite3.connect('character_data.db')

    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO characters (gender, life_stage, voice, aspiration,
                       skin_tone, hair_style, hair_color, eye_color, user_id) 
            VALUES (:Gender, :Life_Stage, :Voice, :Aspiration,
                       :Skin_Tone, :Hair_Style, :Hair_Color, :Eye_Color, :User_Id)
        ''', (character.gender, character.life_stage, character.voice, character.aspiration,
              character.skin_tone, character.hair_style, character.hair_color, character.eye_color, user))
        conn.commit()
        print("Character saved successfully!")
    except sqlite3.IntegrityError:
        print("Character not saved.")
    conn.close()

def get_characters(user, connection=None):
    ''' Hakee tietokannasta kaikki hahmot.
    Returns:
        Kaikki tietokannassa olevat hahmot.
        '''
    conn = connection
    if conn is None:
        conn = sqlite3.connect('character_data.db')

    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM characters WHERE user_id = ?''', (user,))
    characters_data = cursor.fetchall()
    conn.close()

    characters = []
    for data in characters_data:
        character = Character(*data)
        characters.append(character)
    return characters
