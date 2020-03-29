'''
1. Write a function, while_loop(max_number), that contains a while loop that loops
from 1 to n, where n is a positive number (passed as parameter - max_number),
saving the number in a list on each loop. The function shall return the list of all numbers.
If no parameter is passed to the function, while_loop() shall return the list of numbers from 1 to 10:
a. while_loop() -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b. while_loop(5) -> [1, 2, 3, 4, 5]
'''


def while_loop(max_number=10):
    try:
        max_number = int(max_number)
        out = []
        i = 1
        while i <= max_number:
            out += [i]
            i += 1
        return out
    except:
        return 'Not an integer! Or at least not a positive one...'


'''
2. Rewrite the function, while_loop(max_number), so it can also take negative numbers as input 
(passed as parameter - max_number). If a negative number is passed to while_loop(max_number), 
the list shall return the numbers from 1 to the negative number:
a. while_loop(-5) -> [1, 0, -1, -2 ,-3, -4 ,-5]
'''


def while_loop(max_number=10):
    out = []
    i = 1
    if max_number < 0:
        while i >= max_number:
            out += [i]
            i -= 1
    else:
        while max_number >= i:
            out += [i]
            i += 1
    return out


'''
3. Rewrite the function, while_loop(max_number), so it will also add the numbers as 
they go using an accumulator and add this value as the last value in the list:
a. while_loop(5) -> [1, 2, 3, 4, 5, 15]
'''


def while_loop(max_number=10):
    out = []
    i = 1
    acc = 0
    if max_number < 0:
        while i >= max_number:
            acc += i
            out += [i]
            i -= 1
    else:
        while max_number >= i:
            acc += i
            out += [i]
            i += 1
        out += [acc]
    return out


'''
4. Rewrite the function, while_loop(max_number), so irrespective of the value 
of the max_number parameter, the output list will never go higher 
than 12, or lower than -12 (use break):
a. while_loop(14) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78]
'''


def while_loop(max_number=10):
    out = []
    i = 1
    acc = 0
    if max_number < 0:
        # negative
        while i >= max_number:
            acc += i
            out += [i]
            i -= 1
            if i < -12:
                break
        out += [acc]
    else:
        # positive
        while max_number >= i:
            acc += i
            out += [i]
            i += 1
            if i > 12:
                break
        out += [acc]
    return out


'''
5. Rewrite the function, while_loop(max_number), so it takes a 
second parameter (even), a boolean value which when True only adds the 
even numbers to the list (use continue). Similar to the max_number parameter, 
even shall default to False if not passed:
a. while_loop(14,True) -> [2, 4, 6, 8, 10, 12, 42]
b. while_loop(14, False) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78]
c. while_loop() -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55]
'''


def while_loop(max_number=10, even=False):
    out = []
    acc = 0
    if even:
        i = 2
    else:
        i = 1
    if max_number < 0:
        # negative
        while i >= max_number:
            if even:
                acc += i
                out += [i]
                i -= 2
                if i < -12:
                    break
            else:
                acc += i
                out += [i]
                i -= 1
                if i < -12:
                    break
        out += [acc]
    else:
        # positive
        while max_number >= i:
            if even:
                acc += i
                out += [i]
                i += 2
                if i > 12:
                    break
            else:
                acc += i
                out += [i]
                i += 1
                if i > 12:
                    break
        out += [acc]
    return out


'''
6. Finally, add a third parameter (boolean - factorial) to the while_loop function, 
which will add the factorial value of the last number in the while loop as the last parameter 
(do not factorial the accumulator value). It will default to False if not passed. 
Factorial (e.g. 10!) is 10*9*8*7*6*5*4*3*2*1=3628800:
a. while_loop() -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55]
b. while_loop(14, False, True) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 479001600]
c. while_loop(14, even=False, factorial=True) ->
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 78, 479001600]
'''


def while_loop(max_number=10, even=False, factorial=False):
    out = []
    acc = 0
    if even:
        i = 2
    else:
        i = 1
    if max_number < 0:
        # negative
        while i >= max_number:
            if even:
                acc += i
                out += [i]
                i -= 2
                if i < -12:
                    break
            else:
                acc += i
                out += [i]
                i -= 1
                if i < -12:
                    break
        out += [acc]
    else:
        # positive
        while max_number >= i:
            if even:
                acc += i
                out += [i]
                i += 2
                if i > 12:
                    break
            else:
                acc += i
                out += [i]
                i += 1
                if i > 12:
                    break
        out += [acc]
    n = len(out) - 1
    j = 0
    fac = 1
    if factorial:
        while j < n:
            fac *= out[j]
            j += 1
        out += [fac]
    return out
