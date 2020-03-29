'''
1. For each of the following functions, please use for loops, and add comments to your code.
For practice, do not use any inbuilt Python functions which we have not covered in class.
Also make sure you use return and not print if something is to be returned from a function:
'''

'''
a. A stairs is a list of at least two numbers where either:
i. each number is one greater than the previous number or
ii. each number is one smaller than the previous number.
iii. Write a Python function is_stairs( s ) to test if the numeric list s is a
stairs.
iv. is_stairs([2,3,4,5])and is_stairs([8,7,6]) both return TRUE
is_stairs ( [ 2, 3, 5 ] ), is_stairs ( [ 2, 3, 2 ] ), and is_stairs ( [ 4 ] ) all return False.

b. Add additional functionality to is_stairs( s ) to also check for strings in a list ["a", "b", "c"]:
i. is_stairs( s ) will now also test if the letters passed in are next to each other in the alphabet
ii. True for both a-z and the reverse z-a
iii. assume for is_stairs( s ), that input 'A' and 'a' are the same
print(is_stairs(["a", "b", "c"])) 
print(is_stairs(["c", "b", "a"])) 
print(is_stairs(["a", "B", "c"])) 
print(is_stairs(["a", "b", "C"])) 
print(is_stairs(["c", "B", "a"])) 
print(is_stairs(["C", "b", "a"])
'''

def is_stairs(s):

    if len(s) < 2:
        #Blank and one character list are false
        return False

    list = 'down'
    if ord(str(s[0]).lower()) == ord(str(s[1]).lower()) -1:
        list = 'up'
    found = True

    for i in range(len(s)-1):

        if list == 'up':
            if ord(str(s[i]).lower()) != ord(str(s[i+1]).lower()) - 1:
                # For an ascending list
                found = False
                break
        else:
            if ord(str(s[i]).lower()) != ord(str(s[i+1]).lower()) + 1:
                # For an descending list
                found = False
                break
    return found


'''
c. I want you to write a function called: factorial( n ), but unlike Lab 6, the value of n! = 1*2*· · ·*n, 
for any non-negative integer ‘n’ (note that 0! is defined to have the value 1). Factorial of a negative number returns -1
i. Factorial( 3 ) ⇒ 6
Factorial( 1 ) ⇒ 1
Factorial( 0 ) ⇒ 1
Factorial( 40 ) ⇒ 815915283247897734345611269596115894272000000000
'''

def factorial(n):
    fac = 1
    if n < 0:
        return -1
    elif n == 0:
        return fac
    else:
        for num in range(1,n+1):
            fac *= num
        return fac

'''
d. If you've seen Gremlins the movie (from like a million years ago), 
then you know the little furry creatures known as Mogwai must be cared for with consideration for these three rules:

i. Don't get them wet
ii. Don't expose them to bright light.
iii. Don't feed them after midnight.
iv. So, I am giving you a gift of Gizmo, a little furry Mogwai who just loves
to play.
v. I want you to write a function which will determine the faith of Gizmo:


Call the function gremlins(name), passing Gizmo as the name of the Mogwai
anytime you print something to screen reference the name of your Gremlin
use a for or a while loop for 5 loops, each time randomly calling one of the 3 helper functions outlined below and determine the faith of your Mogwai.
return the faith of Gizmo at the end of the 5 loops, but:

a. if okay_to_feed(time) returns False, Gizmo is now a Gremlin called Stripe, reflect this in any print statements
b. if is_too_bright(lux_level) returns True, break out of the loop, as your time with Gizmo/ Stripe is no more.
c. if is_wet() returns True, then Gizmo is now part of a set of triplets, reflect this in any print statements

is_wet() - return true or False
is_too_bright(lux_level) - returns True if lux level is greater 80 okay_to_feed(time) - returns False if after 
midnight (zero) and before 4am (4), using 24 hour clock
Each of these functions, will return a boolean, but I want you to randomly determine the returned answer using 
'import random': random.randint(1,5) returns a value from 1 to 5, while random.choice(['red', 'black', 'green']) 
returns 'red' or 'black' or 'green'.

vii. I want you to have a bit of fun with this, so please do. 
Oh, all input/output must be suitable for me or my professor to read :)

viii. these are some of my sample outputs: 
1. Gizmo is a triplet
2. Stripe rules
3. Stripe is no more 
4. Gizmo is no more 
5. Gizmo
'''
import random

def is_wet():
    return random.choice([True, False])

def is_too_bright(lux_level):
    lux_level = random.randint(0,200)

def okay_to_feed(time):
    time = random.randint(0,23)
    #at midnight the clock goes back to 0, hence 23 and not 24

def gremlins(name):

    for i in range(5):
        func = random.randint(0,2)
        if func == 0:
            if is_wet():
                print(name + ' is a triplet')
            else:
                print(name)
                pass

        elif func == 1:
            lux_level = random.randint(50, 100)
            if lux_level > 80:
                print(name + ' is no more')
            else:
                print(name)
                pass

        else:
            time = random.randint(0, 23)
            if time > 4:
                name = 'Stripe'
                print(name, 'rules')
            else:
                name = 'Gizmo'
                print(name)
                pass
    return ""
    #this stops the loop returning 'none' at the end

gremlins('Gizmo')