import math
import random



def int_check(question, low=None, high=None):
    while True:

        error = "please enter a number"
        if low is not None and high is not None:
            error = f"please enter a number greater than or equal to {low} and less than {high}"
        elif low is not None:
            error = f"please enter a number greater than or equal to {low}"

        to_check = input(question)

        try:
            to_check = int(to_check)

            if low is not None and to_check < low:
                print(error)
            elif high is not None and to_check > high:
                print(error)
            else:
                return to_check

        except ValueError:
            print(error)




def yes_no(question):
    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")


def instructions():
    print("""
    ***** Instructions *****
chose what level you want to play at:
    level 1: easy
    level 2: moderate
    level 3: advanced
    level 4: difficult
    level 5: hard 
after you have chosen a level to play at, 
then you must chose how many rounds you want to play

if at any point you want to exit the game type 
    "xxx"
         """)

def level_check(question):

    level = int_check(question, 1,5)

    if level == 1:
        return "level 1"

    elif level == 2:
        return "level 2"

    elif level == 3:
        return "level 3"

    elif level == 4:
        return "level 4"

    elif level == 5:
        return "level 5"
    else:
        return "level 1"


print("Welcome To The Math Game")

want_instructions = yes_no("Do you want to see the instructions. ")

if want_instructions == "yes":
    instructions()
num_rounds = 1
rounds_played = 0
num_questions = int_check("how many rounds do you want to play ", 1)

level_check("what level do you want to work at? ")


if level_check == "level 1":
    num_rounds += 1
    number_1 = random.randint(1,100)
    number_2 = random.randint(1,100)
    answer_1 = number_1 + number_2
    print(f"Round {num_rounds}")
    print(f"{number_1} + {number_2}")
    user_choice = int_check("answer: ")
    if user_choice == answer_1:
        print("Correct! ")
    else:
        print("Incorrect ")
        print(f"The correct answer was {answer_1}")
        print(f" you lasted {num_rounds} questions")

elif level_check == "level 2":
    num_rounds += 1
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    answer_1 = number_1 - number_2
    print(f"Round {num_rounds}")
    print(f"{number_1} - {number_2}")
    user_choice = int_check("answer: ")
    if user_choice == answer_1:
        print("Correct! ")

    else:
        print("Incorrect ")
        print(f"The correct answer was {answer_1}")
        print(f" you lasted {num_rounds} questions")

elif level_check == "level 3":
    num_rounds += 1
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    answer_1 = number_1 - number_2
    print(f"Round {num_rounds}")
    print(f"{number_1} - {number_2}")
    user_choice = int_check("answer: ")
    if user_choice == answer_1:
        print("Correct! ")

    else:
        print("Incorrect ")
        print(f"The correct answer was {answer_1}")
        print(f" you lasted {num_rounds} questions")

elif level_check == "level 4":
    num_rounds += 1
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    answer_1 = number_1 - number_2
    print(f"Round {num_rounds}")
    print(f"{number_1} - {number_2}")
    user_choice = int_check("answer: ")
    if user_choice == answer_1:
        print("Correct! ")

    else:
        print("Incorrect ")
        print(f"The correct answer was {answer_1}")
        print(f" you lasted {num_rounds} questions")

elif level_check == "level 5":
    num_rounds += 1
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    answer_1 = number_1 - number_2
    print(f"Round {num_rounds}")
    print(f"{number_1} - {number_2}")
    user_choice = int_check("answer: ")
    if user_choice == answer_1:
        print("Correct! ")

    else:
        print("Incorrect ")
        print(f"The correct answer was {answer_1}")
        print(f" you lasted {num_rounds} questions")





