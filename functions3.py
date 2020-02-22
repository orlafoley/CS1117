# ScriptName: functions.py
# Author:
# Student Number:
# template for calling functions in another file

'''
def print_function():
    print("I'm in another file :)")
'''

import math

#Question 1
def three_numbers():
    '''
    three_numbers - function - asks for three numbers
    :param num1: variable, integer, asks for a number
    :param num2: variable, integer, asks for another number
    :param num3: variable, integer, asks for a third number
    :return: prints true/false, depending on whether numbers match ages of myself and my sisters
    '''

    num1 = input("What is my age? ")
    num2 = input("What is my sister's age? ")
    num3 = input("What is my other sister's age? ")
    try:
        num1=int(num1)
        num2=int(num2)
        num3=int(num3)
        if num1 == 19 and num2 == 23 and num3 == 26:
            return True
        else:
            return False
    except:
        return 'That\'s not a number >:('


'''2. Write a function called seasons(), that has a parameter called number.
Ask the user for a number, and pass this number to the function.
Depending on the number passed to the function, the function will displays the corresponding season of the year where
1=Winter, 2=Spring, 3=Summer, and 4 = Autumn. Add code to display an error message if any other number is entered.
'''

#Question 2
#Leaving out int causes an error
def seasons(number=0):
    '''
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4
    '''
    number = input("Give me a number from 1-4: ")
    try:
        number=int(number)
        if number == 1:
            return "Winter"
        elif number == 2:
            return "Spring"
        elif number == 3:
            return "Summer"
        elif number == 4:
            return "Autumn"
        else:
            #number outside specified range
            return "whomst'd've'ly'yaint'nt'ed'ies's'y'es?????"
    except:
        return 'WHERE IS MY NUMBER?'


#Question 3

def grades():
    grade_percentage =input("What percentage did you get in your last test? ")
    try:
        grade_percentage=int(grade_percentage)
        if grade_percentage <= 100 and grade_percentage >= 85:
            return "A"
        elif grade_percentage <= 84 and grade_percentage >= 70:
            return "B"
        elif grade_percentage <= 69 and grade_percentage >= 55:
            return "C"
        elif grade_percentage <= 54 and grade_percentage >= 40:
            return "D"
        elif grade_percentage <= 39 and grade_percentage >= 25:
            return "E"
        elif grade_percentage <= 24 and grade_percentage >= 0:
            return "F"
        else:
            return "X"
    except Exception as e:
        return 'Ah yes, my favourite grade percentage: the ' + str(e)


'''
4. Ask the user for 2 numbers, and pass these 2 numbers to a function called equal_numbers().
If the two numbers are equal, then display the square root of the number (Use import math at the top of your program
to import the math library and use the command math.sqrt()) to get the square root of a
number e.g. math sqrt (25.0) gives 5.0). If the two numbers are not equal, then display the squares of both numbers.
Recall ** for the exponent e.g. 2 ** 3 gives 8.
'''
#Question 4
#Entering letters makes the computer cry

def equal_numbers():
    number1 = int(input("Give me a number, puny human! "))
    number2 = int(input("Give me another number, peasant! "))
    if number1 == number2:
        return math.sqrt(number1), math.sqrt(number2)
    else:
        return (number1) ** 2, (number2) ** 2

#Question 5
def fizz_buzz():
    number = input("Supply me with a whole number: ")
    try:
        number=int(number)
        if (number%3 == 0) and (number%5 == 0):
            return "FizzBuzz"
        elif number%3 == 0:
            return "Fizz"
        elif number%5 == 0:
            return "Buzz"
        else:
            return number
    except:
        number=float(number)
        if type(number)==float:
            return 'That\'s not a whole number...'
        else:
            return 'ANGRY LACK OF NUMBER!'