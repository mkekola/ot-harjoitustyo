import time
from entities.character import Character
from database import init_db, login_user, register_user, save_character, get_characters


def main():
    init_db()
    logged_in = False
    current_user = None

    while True:
        if not logged_in:
            print("\nHooba Noobie! (What's up! in Simlish)\n")
            print("[1] Register")
            print("[2] Login")
            print("[3] Exit\n")

            action = input("What would you like to do? ")

            if action == "1":
                username = input("\nEnter your username: ")
                password = input("Enter your password: ")
                register_user(username, password)

            elif action == "2": 
                username = input("\nEnter your username: ")
                password = input("Enter your password: ")
                current_user = login_user(username, password)
                if current_user:
                    logged_in = True

            elif action == "3":
                print("\nDag Dag!")
                break

            else:
                print("Invalid action.")

        else:
            print("\nSul Sul!")
            print("[1] List created characters")
            print("[2] Generate a new character")
            print("[3] Logout\n")

            action = input("What would you like to do? ")

            if action == "1":
                characters = get_characters(current_user)
                if characters:
                    print("Characters:\n")
                    for character in characters:
                        print(character)
                else:
                    print("No characters found.")

            elif action == "2":
                print("Generating character...\n")
                time.sleep(2)
                random_character = Character()
                print(random_character)
                save_option = input("Would you like to save this character? (yes/no): ")
                if save_option.lower() == "yes":
                    save_character(random_character, current_user)
                else:
                    print("Character not saved.")
            elif action == "3":
                logged_in = False
                current_user = None
            else:
                print("Invalid action.")


if __name__ == "__main__":
    main()
