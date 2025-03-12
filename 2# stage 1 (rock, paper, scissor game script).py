# importing necessary modules
import random

# welcome message to the user
name = input("hello, can I ask for your name please? ")
print(f"glad to meet you, {name}. welcome to our Rock, Paper, Scissor game.\n"
      f"we are thrilled to have you here. let us begin.\n"
      f"\n"
      f"starting with some explanations: you are playing against the computer,\n"
      f"you must choose between the choices rock, paper, or scissor. the rules are as follows:\n"
      f"Paper wins over Rock\n"
      f"Rock wins over Scissor\n"
      f"Scissor wins over Paper\n")

# creating the functions and conditions
def game_function():

    # variables
    choice_list = ['1', '2', '3', 'rock', 'paper', 'scissor']
    computer_choice = random.choice(choice_list)
    computer_wins = 0
    user_wins = 0
    rounds_quantity = input()

    # program messe
    print("you have the following options:\n"
          "1/ Rock\n"
          "2/ Paper\n"
          "3/ Scissor\n")
    print("you can type in the number associated with the choice or the name it as well.\n")
    print("the computer has already chosen its response !!!\n"
          "what will be yours ?\n")

    # variables
    choice_list = ['1', '2', '3', 'rock', 'paper', 'scissor']
    computer_choice = random.choice(choice_list)
    computer_wins = 0
    user_wins = 0
    rounds_quantity = input()

    while True:

        # user input and condition
        user_choice = input("please type in you answer here: ")
        print("\n")

        if user_choice.isdigit() or user_choice.isalpha():
            if user_choice.lower() in choice_list:
                # winning conditions

            else:
                print("your input is invalid.\n"
                      "please try again.\n")
        else:
            print("your input is invalid.\n"
                  "please try again.\n")

# call the function
final = game_function()
print(final)
