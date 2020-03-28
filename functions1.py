#Script Name:   functions1.py
#Author:
#Student Number:

#get the first age

age1 = int(input("Please enter age 1: "))
# get the second age
age2 = int(input("Please enter age 2: "))
# determine the average age
average = (age1+age2)/2
# print to screen
print("The average age is %d" % average)

print("The average age is %d" % ((int(input("Please enter age 1: "))
                                  + int(input("Please enter age 2: ")))/2))


#name asks for the first name, name_2 asks for the surname
#the input function asks the user the question
#we then print hello as a string and then use commas to add in spaces between their first and last names
name = str(input("What is your first name?"))
name_2 = str(input("What is your last name?"))
print("hello", name, name_2)

def ask_for_string_input (question_string):
    '''this function converts the users answer to a string'''
    user_input = str(input(question_string))
    return user_input.lower()

name_1 = ask_for_string_input("What is your first name?")
name_2 = ask_for_string_input("What is your last name?")
print("Hello", name_1.capitalize(), name_2)

my_age = 19
minecraft = "game"
reasons_to_live = "CS1117"
my_friend = "Anne"
my_height = 1.6
my_memes = "dank"
my_roommates = ("Niamh", "Tamara");
minecraft_sheep_height = 1.25
number_of_minecraft_objects_in_bedroom = 4
bedroom_collection = ("Enderman mug", "Creeper", "Enderman", "Zombie");

print(type(my_age))
print(type(my_friend))
print(type(my_height))
print(type(my_memes))
print(type(my_roommates))
print(type(minecraft))
print(type(minecraft_sheep_height))
print(type(number_of_minecraft_objects_in_bedroom))
print(type(bedroom_collection))
print(type(reasons_to_live))


def favourite_game (question_string):
    '''this function will ask the users favourite game'''
    user_input = (input(question_string))
    return user_input

game_1 = favourite_game("What is your favourite game?")
print("Your favourite game is", game_1 + "!")
print(game_1, id(game_1), type(game_1))
