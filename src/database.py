import sqlite3
from entities.character import Character

def open_connection(connection):
    ''' Avaa tietokantayhteyden.
    Args:
        connection: Tietokantayhteys.
    Returns:
        Tietokantayhteys.
    '''
    if connection is None:
        return sqlite3.connect('character_data.db')
    return connection

def close_connection(connection):
    ''' Sulkee tietokantayhteyden.
    Args:
        connection: Tietokantayhteys.
    '''
    if connection is None:
        connection.close()

def init_db(connection=None):
    ''' Alustaa tietokannan, jos sitä ei ole olemassa.
    Args: 
        connection: Tietokantayhteys.
    '''
    conn = open_connection(connection)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,
               username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS characters (id INTEGER PRIMARY KEY,
                   user_id INTEGER, gender TEXT,
                   life_stage TEXT, voice TEXT, aspiration TEXT, skin_tone TEXT,
                   hair_style TEXT, hair_color TEXT, eye_color TEXT, 
                   FOREIGN KEY (user_id) REFERENCES users(id))''')
    conn.commit()
    close_connection(conn)

def register_user(username, password, connection=None):
    ''' Rekisteröi käyttäjän tietokantaan.
    Args:
        username: Käyttäjänimi.
        password: Salasana.
        connection: Tietokantayhteys.
    Returns:
        True, jos rekisteröinti onnistui, muuten False.
    '''
    conn = open_connection(connection)
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO users (username, password) VALUES (:Username, :Password)''',
                       (username, password))
        conn.commit()
        close_connection(conn)
        print("User registered successfully!")
        return True
    except sqlite3.IntegrityError:
        print("Username already exists.")
        close_connection(conn)
        return False

def login_user(username, password, connection=None):
    ''' Kirjaa käyttäjän sisään.
    Args:
        username: Käyttäjänimi.
        password: Salasana.
        connection: Tietokantayhteys.
    Returns:
        Käyttäjän tunniste, jos kirjautuminen onnistui, muuten None.
    '''
    conn = open_connection(connection)
    cursor = conn.cursor()
    cursor.execute('''SELECT id FROM users WHERE username = :Username AND password = :Password''',
                   (username, password))
    user = cursor.fetchone()
    close_connection(conn)
    if user is not None:
        print("Login successful!")
        return user[0]
    print("Login failed.")
    return None

def save_character(character, user, connection=None):
    ''' Tallentaa hahmon tietokantaan.
    Args:
        character: Hahmo, joka tallennetaan tietokantaan.
        user: Käyttäjän tunniste.
        connection: Tietokantayhteys.
    '''
    conn = open_connection(connection)
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO characters (gender, life_stage, voice, aspiration,
                       skin_tone, hair_style, hair_color, eye_color, user_id) 
            VALUES (:Gender, :Life_Stage, :Voice, :Aspiration,
                       :Skin_Tone, :Hair_Style, :Hair_Color, :Eye_Color, :User_Id)
        ''', (character.gender, character.life_stage, character.voice, character.aspiration,
              character.skin_tone, character.hair_style,
              character.hair_color, character.eye_color, user))
        conn.commit()
        print("Character saved successfully!")
    except sqlite3.IntegrityError:
        print("Character not saved.")
    close_connection(conn)

def get_characters(user, connection=None):
    ''' Hakee tietokannasta kaikki hahmot.
    Args:
        user: Käyttäjän tunniste.
        connection: Tietokantayhteys.
    Returns:
        Kaikki tietokannassa olevat hahmot.
    '''
    conn = open_connection(connection)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM characters WHERE user_id = ?''', (user,))
    characters_data = cursor.fetchall()
    close_connection(conn)

    characters = []
    for data in characters_data:
        character = Character(*data)
        characters.append(character)
    return characters
