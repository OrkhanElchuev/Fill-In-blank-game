level_easy = """If we wanted a random integer, we can use the __1__ function.
Randint accepts __2__ parameters: a lowest and a __3__ number.
Generate integers between 1,5.
The first value should be __4__ than the second.\n"""
answer_easy = ["randint", "two", "highest", "less"]

level_medium = """A __1__ is a block of organized, reusable code
that is used to perform a single, related action.
Functions provide better modularity for your application and a
high degree of code __2__ gives you many
__3__ functions like print(), etc. but you can also create your own __4__.
These functions are called user-defined functions\n"""
answer_medium = ["function", "reusing", "built-in", "functions"]

level_hard = """Classes provide a means of bundling data and
functionality together. Creating a new class creates a new type of __1__,
allowing new instances of that type to be made.
Each __2__ instance can have __3__ attached to it for maintaining its state.
Class instances can also have __4__
(defined by its class) for modifying its state.\n"""
answer_hard = ["object", "class", "attributes", "methods"]


def replay():
    # This function asks the user whether he wants to repeat the game
    # and acts according to the input
    user_input1 = raw_input("Would you like to play again?. Enter yes or no: ")
    if user_input1 == "yes":
        return start()
    elif user_input1 == "no":
        print "\nThank you for playing! Have a good day!"
        print "Press any key to exit.\n"
        raw_input()
    else:
        print "\nYour input is not valid(yes, no). Please,try again!"
        return replay()


def check_input(player_input, ans):
    # Check whether player's input is correct or not.
    # Return True or False according to the input.
    if player_input == ans:
        print "\nYou are right!\n"
        return True
    else:
        print "\nInvalid. Please, try again."
        return False


def gamebody(level, answer):
    # The main function which prints the article(according to the difficulty)
    # then checks for user input and modifies
    # the article according to the input's validity
    replace_me_quantity = ["__1__", "__2__", "__3__", "__4__"]
    print "\n\n" + level
    index = 0
    while index < len(replace_me_quantity):
        if replace_me_quantity[index] in level:
            player_input = raw_input(
            "What would you put in " + replace_me_quantity[index] + " : ")
            if check_input(player_input, answer[index]) is True:
                level = level.replace(replace_me_quantity[index], player_input)
                print level
            else:  # - 1 from index if the input is incorrect
                index -= 1
        index += 1  # + 1 to index to stay at the same question
    print "\nGame finished! Thank you for playing!"
    return replay()


def start():
    # Display the game menu where the user can choose the difficulty level
    # Difficulty levels:(easy,medium,hard). Set the difficulty level.
    print "Welcome to 'Fill In The Blanks' game created by Orkhan Elchuev.\n"
    user_input = raw_input("Enter the difficulty level: easy, medium, hard: ")

    if user_input == "easy":
        return gamebody(level_easy, answer_easy)
    elif user_input == "medium":
        return gamebody(level_medium, answer_medium)
    elif user_input == "hard":
        return gamebody(level_hard, answer_hard)
    else:
        print "\nYour input is invalid. Please, try again!"
        return start()


start()
