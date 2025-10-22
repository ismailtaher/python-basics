#
# String data type
#

# literal assignment
first = 'Ismail'
last = 'Mirza'

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function for value assignment

# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatination
fullname = first + " " + last
print(fullname)

# casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

print("i like rock music from the " + decade + 's')

# multiple lines
multilines = '''
Hey, how are you?

I was just checking in.
                                All good?
'''
print(multilines)

# escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#
# String methods
#

print(first)

# lower case
print(first.lower())
# upper case
print(first.upper())
# does not change the original value but give a new value
print(first)
# capitalize first letter of every word in the string/multiline-string
print(multilines.title())
# replace any word in a string
print(multilines.replace("good", "ok"))

# once again these methods would not change the original value
print(multilines)

# length of the string
print(len(multilines))
# adding some whitespace at the end
multilines += "                                           "
# adding some whitespace at the start
multilines = "                      " + multilines
print(len(multilines))  # again checking length

# removing any whitespace from a string
print(len(multilines.strip()))
print(len(multilines.lstrip()))
print(len(multilines.rstrip()))

print("")  # just extra line to seperate all the outputs above

# build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(15, ".") + "$1".rjust(5))
print("Muffin".ljust(15, ".") + "$2".rjust(5))
print("Cheesecake".ljust(15, ".") + "$4".rjust(5))

print('')
# string index values
print(first[0])
print(first[1])
print(first[-1])
print(first[2:-1])
