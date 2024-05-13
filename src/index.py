import time
from entities.character import Character
from database import init_db, login_user, register_user, save_character, get_characters

def menu_view():
    print("\nHooba Noobie! (What's up! in Simlish)\n")
    print("[1] Register")
    print("[2] Login")
    print("[3] Exit\n")
    action = input("What would you like to do? ")
    return action


def new_register_user():
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")
    register_user(username, password)


def login_input_view():
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")
    user = login_user(username, password)
    return user


def app_view():
    print("\nSul Sul! (Hello! in Simlish)\n")
    print("[1] List created characters")
    print("[2] Generate a new character")
    print("[3] Logout\n")
    action = input("What would you like to do? ")
    return action


def list_characters(user):
    characters = get_characters(user)
    if characters:
        print("Characters:\n")
        for character in characters:
            print(character)
    else:
        print("No characters found.")


def create_character_view(user):
    print("Generating character...\n")
    time.sleep(2)
    random_character = Character()
    print(random_character)
    save_option = input("Would you like to save this character? (yes/no): ")
    if save_option.lower() == "yes":
        save_character(random_character, user)
    else:
        print("Character not saved.")


def main():
    init_db()
    logged_in = False
    current_user = None

    while True:
        if not logged_in:
            action = menu_view()

            if action == "1":
                new_register_user()

            elif action == "2":
                current_user = login_input_view()
                if current_user:
                    logged_in = True

            elif action == "3":
                print("\nDag Dag! (Goodbye! in Simlish)\n")
                break

            else:
                print("Invalid action.")

        else:
            action = app_view()

            if action == "1":
                list_characters(current_user)

            elif action == "2":
                create_character_view(current_user)

            elif action == "3":
                logged_in = False
                current_user = None
            else:
                print("Invalid action.")


if __name__ == "__main__":
    main()
