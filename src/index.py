import time
from character import create_random_character
from database import init_db, save_character, get_characters

def create_character():
    character = character.create_random_character()
    save_character(character)
    return character

def main():
    init_db() # Initialize the database

    print("Generating character...")
    time.sleep(2) # Simulate processing time

    # Generate a random character
    random_character = create_random_character()

    # Print the generated character
    for attribute, value in random_character.items():
        print(f"{attribute}: {value}")

    # Ask the user if they want to save the character
    saving_option = input("Would you like to save this character? (yes/no): ")
    if saving_option.lower() == "yes":
        save_character(random_character)
        print("Character saved successfully!")
    else:
        print("Character not saved.")

if __name__ == "__main__":
    main()