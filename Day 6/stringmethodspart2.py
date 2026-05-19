# isdecimal()
# isdigit()
# isnumeric()

# isdecimal
# Returns true if all characters in a string are decimal characters (0-9 only)
# They are strictly digit used to form base -10 numbers
# Base-10 numbers also known as decimal numbers, use the digit 0 to 9 to represent any numbers
# It is the number system we commonly used.
# Does not consider superscripts, fraction or roman numbers as valid decimals.

# print('1234'.isdecimal())
# print('1234.56'.isdecimal())
# print('① ② ③ ④'.isdecimal())

# isdigit()
# Returns True if all characters are digit.
# Digits includes decimal digits(0-9)
# Allow other digits characters such as superscripts, subscript digit or digits from numeral systems
# Does not consider superscripts, fraction or roman numbers as valid decimals.

# print('1234'.isdigit())
# print('¹²³'.isdigit())
# print('①'.isdigit())
# print('①②③④'.isdigit())
# print('1234.56'.isdigit())

# isnumeric()

# Returns true if all characters are numeric.
# This is the broadest check - includes digits, decimals, roman numerals, currency numerators,etc
# Accepts everything isdecimal() and isdigit() accepts, plus additional numeric characters.

# print('1234'.isnumeric())
# print('¹²³'.isnumeric())
# print('①'.isnumeric())
# print('½'.isnumeric())
# print('1234.56'.isnumeric())
# print('Ⅸ'.isnumeric())

#split(): Spliting strings

#list of delimeters - space, @. #, &, (), -, :, ;

# s= 'abc@gmail.com'
# lst=s.split('@')
# print(type(lst))
# print(lst)
# print(lst[0])
# print(lst[1])

#Example

# s='one,two,three'
# lst=s.split(',')
# print(lst)
# print(lst[0])
# print(lst[1])
# print(lst[2])

#startwith() - returns true or false

# s='welcome'
# print(s.startswith('wel'))
# print(s.startswith('Wel'))

#endswith() - return true or false

# print(s.endswith('come'))
# print(s.endswith('Come'))

#Trimming spaces - strip(), lstrip(), rstrip()

s='   hello   '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
