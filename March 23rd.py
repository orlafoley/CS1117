# this week we will use a Python dictionary to implement a regular
# language-to-language dictionary. For example, a ( very short )
# English-to-Irish dictionary could be implemented in Python as:
# { "sun":"grian", "water":"uisce", "horse":"capall", "tree":"crann" }

# create a function called:
#   read_dictionary( filename )
# with 1 parameters called:
#   filename - string name of file
# which will read the file ‘filename’, which should contain two words per line,
# and return a dictionary with the first words as keys and the corresponding
# second words as values

# create a function called:
#   inverse( d )
# with 1 parameters called:
#   d - dictionary
# which returns a copy of the dictionary ‘d’ but with keys and values interchanged.
# For example, calling ‘Inverse’ on the above English-to-Irish dictionary
# should produce the equivalent Irish-to-English dictionary:
# { "uisce":"water", "crann":"tree", "grian":"sun", "capall":"horse" }

# create a function called:
#   print_dictionary( d )
# with 1 parameters called:
#   d - dictionary
# which prints the output the dictionary ‘d’, sorted alphabetically by keys,
# with one key-value pair per line, formatted as left-justified columns of width 10.

# For example, the above dictionary should be output as:
#       horse     : capall
#       sun       : grian
#       tree      : crann
#       water     : uisce

def read_dictionary(filename):
    """
    :param filename: takes in a file name in '' and ends in .txt
    :return: a dictionary that translates Irish words to English
    """
    words_in = open('filename.txt', 'r')
    # dictionary is read in
    lines = words_in.readlines()
    d = {}
    words_in.close()
    for line in lines:
        line=line.strip('\n').split(' ')
        #possibly needs to be amended for larger data that may have spacing between two words of the same language
        d[line[0]] = line[1]
    return d

print(read_dictionary('filename.txt'))

def inverse(d):
    reverse_d = {}
    keylist = []
    valuelist = []
    for value in d.keys():
        valuelist += [value]
    for key in d.values():
        keylist += [key]
    for i in range(len(keylist)):
        reverse_d[keylist[i]] = valuelist[i]
    return reverse_d

print(inverse(read_dictionary('filename.txt')))

# create a function called:
#   print_dictionary( d )
# with 1 parameters called:
#   d - dictionary
# which prints the output the dictionary ‘d’, sorted alphabetically by keys,
# with one key-value pair per line, formatted as left-justified columns of width 10.

# For example, the above dictionary should be output as:
#       horse     : capall
#       sun       : grian
#       tree      : crann
#       water     : uisce

def print_dictionary(d):
    out = ''
    space = '          '
    for english, irish in d.items():
        if len(english)>3:
            out += ('%s %s \t : %s \n' % (space, english, irish))
        else:
            out += ('%s %s \t \t : %s \n' % (space, english, irish))
    return out

print(print_dictionary(read_dictionary('filename.txt')))