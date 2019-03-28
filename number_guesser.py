import random


def random_number_roll():
    random_num = random.randint(1, 10)
    return random_num


def main():
    number = True
    print("Welcome to the number guesser!")
    while number:
        answer = input("Please input a number between "
                       "1-10 or press 'q' to quit.")

        if answer == "q":
            number = False
            print("Thank-you for playing, goodbye.")
        elif answer == random_number_roll():
            print("I think you chose: " + str(random_number_roll()) + " I am a psychic!")
            print("I am a psychic!")
        else:
            print("What?! You chose " + str(random_number_roll()) + "? " +
                  "Let, me try again. I have failed as a psychic!")


main()

