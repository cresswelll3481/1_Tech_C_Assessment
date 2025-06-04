import math
import random



#checks numbers
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



#checks between yes and no
def yes_no(question):
    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")


# where instructions are put
def instructions():
    print("""
    ***** Instructions *****
you must chose how many rounds you want to play
then enter the answer to the questions displayed 

if you would like to see your game history then answer yes to the prompt at the end of your game

         """)


# Main routine
print("Welcome To The Math Game")

want_instructions = yes_no("Do you want to see the instructions. ")

if want_instructions == "yes":
    instructions()


num_rounds = 0
rounds_played = 0
correct = 0
incorrect = 0
#logs game history
game_history = []

#asks user how many questions they want to play
num_questions = int_check("how many rounds do you want to play ", 1)

#main game here
while num_rounds < num_questions:
    num_rounds += 1
    number_1 = random.randint(1,100)
    number_2 = random.randint(1,100)
    print(f"Round {num_rounds}")

    # chooses from +, -, *
    op = random.randint(1,3)
    if op == 1:
        var = '+'
        answer = number_1 + number_2
    elif op == 2:
        var = '-'
        answer = number_1 - number_2
    elif op == 3:
        var = '*'
        answer = number_1 * number_2

    print(f"{number_1} {var} {number_2}")

    user_choice = int_check("answer: ")
    if user_choice == answer:
        print("Correct! ")
        correct += 1
    else:
        print("Incorrect ")
        print(f"The correct answer was {answer}")
        incorrect += 1


#asks user if they want to see their results
ask_result = yes_no("do you want to see your results? ")
game_result = f"you lasted {num_rounds} and got {correct} correct, and you got {incorrect} incorrect. "

game_history.append(game_result)
#prints game history
if ask_result == "yes":
    print("game history")
    for item in game_history:
        print(item)




