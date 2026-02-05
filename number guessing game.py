print("...Number guessing game...")

import random 
def name():
    user_name = input("Enter your name: ")
    return user_name
def main():
    user_name = name()
    print(f"Welcome {user_name}")
    while True:
        print("Menu: \n1.New game\n2.Game history\n3.Exit")
        choice = int(input("Enter your choice 1-3: "))
        try:
            if choice == 1:
                print(f"{user_name}, you are playing number guessing game ")
                playing_game(user_name)
                return
            elif choice == 2:
                view_history()
                return
            elif choice == 3:
                print("Exiting...")
                break
        finally:
            print("Invalid choice, try again")
def generate_number():
    return random.randint(1,100)
def playing_game(user_name):
    random_number = generate_number()
    attempts = 10
    while attempts > 0:
        user_number = int(input(" Enter your number 1-100: "))
        attempts -= 1
        if user_number < random_number:
            print("Your number is small, please try again ")
        elif user_number > random_number:
            print("Your number is larger than the guessing number , please try again ")
        else:
            print("wow, correct answer, you won the game ")
            with open("game.txt","a") as file:
                        file.write(f"{user_name} won the game\n")
            return
        if attempts == 0:
            print("No attempts are left, you lose the game")
            with open("game.txt","a") as file:
                file.write(f"{user_name} lost the game\n")
                return
def view_history():
    with open("game.txt") as file:
        data = file.read()
        print(data)
main()