# practice 9
# create a program that creates a list by the user. modifies the list by allowing the user to add, slice, and remove items from the previously created list.
# user_list function
def user_list():
    list = []
    n = 1
    while n <= 5:
        value = input("please provide a number here: ")
        if value.isdigit():
            list.append(value)
            n += 1
        else:
            print("")
            print("** the value provided is not a number.\n"
                  "   please try again.")
            print("")
    return list

# program function
def program():
    options = {"A":"append" , "B":"insert" , "C":"pop" }
    while True:
        choice = input("please type in the action you want to take: ")
        if choice in options:
            # choice A
            if choice == "A":
                user_input = input("please provide a number to be added to the list: ")
                if user_input.isdigit():
                    list_result.append(user_input)
                    return list_result
                else:
                    print("")
                    print("** your input was not valid.\n"
                          "   make sure to print a number only.\n")
            # choice B
            elif choice == "B":
                user_input = input("please provide a number to be inserted to the list: ")
                user_index = input("please provide an index for the value to be placed at\n"
                                   "warning: the indexes in the list start from 0 and increase by 1.\n"
                                   "--> ")
                if user_input.isdigit() and user_index.isdigit():
                    list_result.insert(int(user_index), user_input)
                    return list_result
                else:
                    print("")
                    print("** your input was not valid.\n"
                          "   make sure to print a number only.\n")
            # choice C
            elif choice == "C":
                user_input = input("please provide an index for a value to be removed from the list\n"
                                   "warning: the indexes in the list start from 0 and increase by 1.\n"
                                   "--> ")
                if user_input.isdigit():
                    list_result.pop(int(user_input))
                    return list_result
                else:
                    print("")
                    print("** your input was not valid.\n"
                          "   make sure to print a number only.\n")
        else:
            print("")
            print("** your input is not valid.\n"
                  "   your answer can only be A, B and C.\n")
# where the program begins
print("hello dear user. this program is designed to do a bunch of things with lists\n"
      "using pythong as the language to operate. now here is what you will do. you will\n"
      "provide our program with a few numbers, so we can create a list out of it. then\n"
      "you will modify that list. we will offer you some options and you will change the\n"
      "list based on your choosing.\n"
      "shall we begin. then let's go :)")
print("")

list_result = user_list()
print(f"your list is: {list_result}")
print("")

print("now please choose an action from the following options to modify your list.\n"
      "A: append a new character to the list\n"
      "B: Insert a new character in a specific index within the list\n"
      "C: remove a specific character from a specific index\n"
      "\n"
      "type in the alphabet associated with the action you want to take.\n")
print("")

final_result = program()
print(f"this is the final result of your actions: {final_result}")