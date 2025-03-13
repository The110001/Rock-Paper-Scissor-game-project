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
# function for the number of rounds the player wants to play
def rounds():
    # messages to the user
    print("now, we need to know how many rounds you want to play?\n"
          "you can play as many rounds as you like, even a thousand !!\n")
    # number of rounds
    while True:
        number_of_rounds = input("just provide the number right here? ")
        print("\n")
        if number_of_rounds.isdigit():
            return int(number_of_rounds)
        else:
            print("the value you provided is either a word or has\n"
                  "unacceptable characters such as @, ., ! and etc.\n"
                  "please try again.\n")

# the game function
def game_function(rounds_input):

    # variables
    choice_list = ['rock', 'paper', 'scissor']
    computer_wins = 0
    user_wins = 0
    counting_rounds = rounds_input

    # program messages
    print("you have the following options:\n"
          "1/ Rock\n"
          "2/ Paper\n"
          "3/ Scissor\n")
    print("you can type in the name of the option of your choosing.\n")
    print("the computer has already chosen its response !!!\n"
          "what will be yours ?\n")

    while counting_rounds > 0:

        computer_choice = random.choice(choice_list)

        # user input and condition
        user_choice = input("please type in you answer here: ")
        print("\n")

        if user_choice.isalpha():
            if user_choice.lower() in choice_list:

                # winning conditions
                # 1: rock condition
                if user_choice.lower() == "rock":
                    if user_choice.lower() == computer_choice:
                        print("this is a DRAW\n"
                              "you both chose ROCK!\n"
                              f"{counting_rounds} rounds are left.\n")
                    elif user_choice.lower() != computer_choice and computer_choice == "paper":
                        computer_wins += 1
                        counting_rounds -= 1
                        print("this is computer's WIN\n"
                              "you chose ROCK but computer chose PAPER!\n"
                              f"{counting_rounds} rounds are left.\n")
                    elif user_choice.lower() != computer_choice and computer_choice == "scissor":
                        user_wins += 1
                        counting_rounds -= 1
                        print("this is your WIN\n"
                              "you chose ROCK but computer chose SCISSOR!\n"
                              f"{counting_rounds} rounds are left.\n")

                # 2: paper condition
                if user_choice.lower() == "paper":
                    if user_choice.lower() == computer_choice:
                        print("this is a DRAW\n"
                              "you both chose PAPER!\n"
                              f"{counting_rounds} rounds are left.\n")
                    elif user_choice.lower() != computer_choice and computer_choice == "scissor":
                        computer_wins += 1
                        counting_rounds -= 1
                        print("this is computer's WIN\n"
                              "you chose PAPER but computer chose SCISSOR!\n"
                              f"{counting_rounds} rounds are left.\n")
                    elif user_choice.lower() != computer_choice and computer_choice == "rock":
                        user_wins += 1
                        counting_rounds -= 1
                        print("this is your WIN\n"
                              "you chose PAPER but computer chose ROCK!\n"
                              f"{counting_rounds} rounds are left.\n")

                # 3: scissor condition
                if user_choice.lower() == "scissor":
                    if user_choice.lower() == computer_choice:
                        print("this is a DRAW\n"
                              "you both chose SCISSOR!\n"
                              f"{counting_rounds} rounds are left.\n")
                    elif user_choice.lower() != computer_choice and computer_choice == "rock":
                        computer_wins += 1
                        counting_rounds -= 1
                        print("this is computer's WIN\n"
                              "you chose SCISSOR but computer chose ROCK!\n"
                              f"{counting_rounds} rounds are left.\n")
                    elif user_choice.lower() != computer_choice and computer_choice == "paper":
                        user_wins += 1
                        counting_rounds -= 1
                        print("this is your WIN\n"
                              "you chose SCISSOR but computer chose PAPER!\n"
                              f"{counting_rounds} rounds are left.\n")
            else:
                print("your input is invalid.\n"
                      "please try again.\n")
        else:
            print("your input is invalid.\n"
                  "please try again.\n")

    # return of final results
    if user_wins == computer_wins:
        return f"IT IS A DRAW !! you won {user_wins} rounds and the computer won {computer_wins} rounds"
    elif user_wins > computer_wins:
        return f"IT IS YOUR WIN !! you won {user_wins} rounds and the computer won {computer_wins} rounds"
    else:
        return f"IT IS COMPUTER'S WIN !! you won {user_wins} rounds and the computer won {computer_wins} rounds"

# call the functions
user_rounds = rounds()

# message after the number of rounds input
print(f"OK then ! {user_rounds} rounds it is.\n")

final_result = game_function(user_rounds)
print(final_result)