# ScriptName: functions.py
# Author:
# Student Number:

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")

def seasons():
    seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4

    number = input("Give me a number from 1-4: ")
    try:
        number=int(number)
        if number == 1:
            return seasons[number-1]
        elif number == 2:
            return seasons[number-1]
        elif number == 3:
            return seasons[number-1]
        elif number == 4:
            return seasons[number-1]
        else:
            #outside range
            return "whomst'd've'ly'yaint'nt'ed'ies's'y'es?????"
    except:
        return 'That wasn\'t a number bro!'

def grades():
    import math
    grade_percentage = input("What percentage did you get in your last test? ")
    try:
        if type(grade_percentage)==float or type(grade_percentage)==int:
            if type(grade_percentage)==float:
                grade_percentage=math.floor(grade_percentage)
                #round the percentage down to the lower number
                if 100 >= grade_percentage >= 85:
                    return "A"
                elif 84 >= grade_percentage >= 70:
                    return "B"
                elif 69 >= grade_percentage >= 55:
                    return "C"
                elif 54 >= grade_percentage >= 40:
                    return "D"
                elif 39 >= grade_percentage >= 25:
                    return "E"
                elif 24 >= grade_percentage >= 0:
                    return "F"
                else:
                    return "The input numerical grade is outside the range supported"
            else:
                    if 100 >= grade_percentage >= 85:
                        return "A"
                    elif 84 >= grade_percentage >= 70:
                        return "B"
                    elif 69 >= grade_percentage >= 55:
                        return "C"
                    elif 54 >= grade_percentage >= 40:
                        return "D"
                    elif 39 >= grade_percentage >= 25:
                        return "E"
                    elif 24 >= grade_percentage >= 0:
                        return "F"
                    else:
                        return "The input numerical grade is outside the range supported."
    except:
        return 'That is not a number!'

    grade_letter = input("What grade did you get in your last test? ")
    try:
        grade_letter=grade_letter[0].upper()
        if grade_letter == 'A':
            return "85-100"
        elif grade_letter == 'B':
            return "70-84"
        elif grade_letter == 'C':
            return "55-69"
        elif grade_letter == 'D':
            return "40-54"
        elif grade_letter == 'E':
            return "25-39"
        elif grade_letter == 'F':
            return "0-24"
        else:
            return "The input letter grade is outside the range supported"
    except:
        return 'Grade must be a letter!'


def fizz_buzz(divisor_1=3, divisor_2=5):
    number = input("Give me a whole number: ")
    try:
        number=int(number)
        #jumps to except if letters entered
        if (number % divisor_1 == 0) and (number % divisor_2 == 0):
            return "FizzBuzz"
        elif number % divisor_1 == 0:
            return "Fizz"
        elif number % divisor_2 == 0:
            return "Buzz"
        else:
            return number
    except:
        number=float(number)
        if number:
            return 'Too floaty, not int-y enough!'
        else:
            return 'I\'m pretty sure that was not a number'


def slice_reverse():
    user_input = input("Give me a string! ")
    try:
        user_input=str(user_input)
        if (user_input[::-1] == user_input):
            return True
        else:
            return False
    except Exception as e:
        return 'You failed because the error message ' + str(e) + ' cropped up.'

def add_to_list(value, list):
    try:
        value=int(value)
        list=[int(i) for i in list]
        #checks that everything entered into the function is an integer so it won't crash
        if value in list:
            list.sort()
            return list
        else:
            list.append(value)
            list.sort()
            return list
    except Exception as error_message:
        return 'This failed as per error message: ' + str(error_message) + '.'