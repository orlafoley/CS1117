'''
a. count(list, value) - function to return the number of times value occurs in list 
i. count("hello", "l") -> 2
'''






def count(list, value):
    try:
        count = 0
        for char in list:
            if char == value:
                count += 1
        return count
    except:
        return 'Input not iterable.'







'''
b. index(list, value) - function to return the first index that value occurs in list. Return -1 if the value does not occur in the list
i. index("hello", "o") -> 4
ii. index("hello", "p") -> -1
'''




def index(list, value):
    try:
        for char in list:
            if char == value:
                return list.index(value)
        return -1
    except:
        return 'Input not iterable.'





'''
c. get_value(list, index) - function to return the value that occurs in the list at index
i. get_value("hello", 1) -> "e"
'''




def get_value(list, index):
    try:
        if index < len(list):
            return list[index]
        else:
            return 'There is no index ' + str(index) + ' in ' + str(list) + '.'
    except:
        return 'Input must be iterable.'






'''
d. insert(list, index, value) - function to return list, after you have added value at index (
remember to check the length of the list and if index is larger than len(list) add as a new index at the end of list)
i. insert("hello", 1, "a") -> "hallo"
ii. insert("hello", 5, "p") -> "hellop"
'''





def insert(list, index, value):
    try:
        if len(list) <= index:
            return str(list) + str(value)
        else:
            return str(list[:index]) + str(value) + str(list[index+1:])
    except:
        return 'Input is not iterable.'




'''
e. value_in_list(list, value) - function to return True or False if value occurs in list
i. we can then use "if value_in_list(list, value):" as a boolean check
ii. value_in_list("hello", "o") - True
iii. value_in_list("hello", "a") - False
'''




def value_in_list(list, value):
    try:
        for char in list:
            if value in list:
                return True
        return False
    except:
        return 'Input needs to be iterable.'




'''
f. concat(list1, list2) - function to return a new list, which is a combination of list1 and list2
i. concat("hello", " world") -> "hello world"
'''




def concat(list1, list2):
    try:
        return str(list1) + ' ' + str(list2)
    except:
        return 'Error :('




'''
g. remove(value, list) - function to return list with the first occurrence of value removed from list
i. remove("hello", "o") -> "ello"
'''




def remove(list, value):
    try:
        if value in list:
            index = list.index(value)
            return list[:index] + list[index+1:]
        return list
    except:
        return 'Input needs to be iterable.'