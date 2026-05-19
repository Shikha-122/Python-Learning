# capititalize() # Convert first characters into upper case

# s='hello'
# print(s.capitalize())

# casefold()
# converts strings to lower case
s = 'Hello'
# print(s.casefold())
# print(s.lower())

# print(s.upper())

# title() convert first character of each word into uppercase

# s='hello welcome to python'
# print(s.title())

# swapcase() -- swap case lower to upper and upper to lower character.

# s='Hello Welcome To Python'
# print(s.swapcase())

# center: Return a centered a string

# str='banana'
# print(str.center(10))
# print(str.center(10,'*'))\

# format() : format specified value in a string

# name='Johnson'
# print(f'Hello {name}')

# find() Searches the string for a specified values and return the position of where it was found.

# s='hello'
# print(s.find('e')) #1
# print(s.find('l')) #2
# print(s.find('x')) #-1

# index() Searches the string for a specified values and return the position of where it was found.

# s='hello'
# print(s.index('e')) #1
# print(s.index('l')) #2
# print(s.index('x')) #ValueError

# count() Returns the number of times a specified value occurs in a string

# s='banana'
# print(s.count('a'))
# print(s.count('na'))

# replace() --- Returns a string where specified value is replaced with specified value.

# s='hello world'
# print(s.replace('world', 'python'))
# print(s.replace('o', 'p'))

# isalnum --- Returns true if all characters in the strings are alphanumeric (no punctuation or space)
# s='ABC123'
# print(s.isalnum())
#
# s='abc!'
# print(s.isalnum())

# isalpha --- Returns true if all characters in the strings are in the alphabet

# s='Hello'
# print(s.isalpha())
#
# s='123'
# print(s.isalpha())

# isdecimal() --- Returns true if all characters are decimal (0-9)

# s='123'
# print(s.isdecimal())
#
# s='123.33'
# print(s.isdecimal())
#
# s='xyz'
# print(s.isdecimal())

# isdigit() Returns true if all the characters are digits , otherwise false

# s='123'
# print(s.isdigit())
#
# s='123abc'
# print(s.isdigit())

# isnumeric() Returns true if all the characters are numeric (0-9) , otherwise false
# '-1' and '-1.5' are not considered numeric value, because all the characters in the string must be numeric.
# and the '-' and the '.' are not.

# s='123'
# print(s.isnumeric())
#
# s='abc'
# print(s.isnumeric())
#
# s='123.5'
# print(s.isnumeric())

# islower() and isupper()

s = 'hello'
print(s.islower())
print(s.isupper())