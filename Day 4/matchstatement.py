# The match statement is to perform different actions based on different actions
#Instead of writting many if..else statements, you can use the match statement.

#Example 1

# day=10
#
# match day:
#     case 1: print('Sunday')
#     case 2: print('Monday')
#     case 3: print('Tuesday')
#     case 4: print('Wednesday')
#     case 5: print('Thursday')
#     case 6: print('Friday')
#     case 7: print('Saturday')
#     case _:print('Invalid day')

#Example 2
#use pipe characters | as an or operator in the case of evaluation to check for more than one value in one case:

# day=70
#
# match day:
#     case 2|3|4|5|6 : print("Weekdays")
#     case 1|7: print("Weekends")
#     case _: print('Invalid day')


#Assignments

colour= input('Enter the colour:').strip().lower()
match colour:
    case 'red': print('stop')
    case 'yellow': print('wait')
    case 'green': print('go')
    case _: print('Invalid')