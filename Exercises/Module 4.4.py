import random


def guess_game():
    number = random.randint(1, 10)

    while True:
        user_guess = input("Guess a number between 1 and 10: ")

        if user_guess.isdigit() and 1 <= int(user_guess) <= 10:
            user_guess = int(user_guess)
            if user_guess < number:
                print("Too low")
            elif user_guess > number:
                print("Too high")
            else:
                print("Correct")
                break
        else:
            print("Please enter a valid number between 1 and 10.")


guess_game()
