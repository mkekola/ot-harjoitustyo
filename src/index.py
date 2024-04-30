import time
from entities.character import Character
from database import init_db, save_character, get_characters


def main():
    ''' Luo ja tallentaa satunnaisen hahmon. '''

    init_db()  # Initialize the database

    # Ask the user if they want to list created characters
    listing_option = input(
        "Would you like to list created characters? (yes/no): ")
    if listing_option.lower() == "yes":
        characters = get_characters()
        if characters:
            print("Characters:\n")
            for character in characters:
                print(character)
        else:
            print("No characters found.")

    # Ask the user if they want to generate a new character
    generating_option = input(
        "Would you like to generate a new character? (yes/no): ")
    if generating_option.lower() != "yes":
        print("Sul Sul!")
        return

    print("Generating character...\n")
    time.sleep(2)  # Simulate processing time

    # Generate a random character
    random_character = Character()
    print(random_character)

    # Ask the user if they want to save the character
    saving_option = input("Would you like to save this character? (yes/no): ")
    if saving_option.lower() == "yes":
        save_character(random_character)
        print("Character saved successfully!")
    else:
        print("Character not saved.")


if __name__ == "__main__":
    main()
