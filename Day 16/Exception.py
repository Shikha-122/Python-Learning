
#Example 1:

# print('w' # causing the error

#Example 2: Exception

# n=10
# res=n/0 #ZeroDivisionError: division by zero
# print(res)

#Example 3

# x='10'
# # x=int(10)
# x=int('wel') #Value Error
# print(x+5)
# TypeError: can only concatenate str (not "int") to str

#Example 4: Handing expection using try & except

# print('started.....')
# print(x) #NameError: name 'x' is not defined
# print('finished')

# print('started.....')
# try:
#     print(x)
#
# except:
#     print('An exception occurred...')
#
# print('finished')


#Example 5: many exception (we can define multiple  exception for single try)
# try:
#     print(x)
#
# except NameError:
#     print('Variable x is not defined')
# except:
#     print('some other exception')

#Example 6: else with try

#we can use the else keyword to define a block of code to be excecuted if no error were raised

# try:
#     #print('Hello')
#     100/0
#
# except:
#     print('Something went wrong')
# else:
#     print('Nothing went wrong')

# Example 7: finally

# The finally block, if specified , will be executed regardless if try block raises , an error

# try:
#     # print(x)
#     print('welcome')
# except:
#     print('Something went wrong')
# finally:
#     print('This is finally block....')

#Example 8: try, except, else, finally

# try:
#     n=int(input('Enter a value'))
#     res=100/n
# except ZeroDivisionError:
#     print('You cannot divide by Zero')
# except ValueError:
#     print('Enter a valid number....')
# else:
#     print(res)
# finally:
#     print('Exception Completed')

#Example 9: try inside another try

# try:
#     file=open('C://Users//prai3//Desktop//myfile.txt','r')
#     try:
#         file.write('welcome')
#     except:
#         print('Something went wrong when writting data into file')
#     finally:
#         file.close()
# except:
#     print('Something went wrong while opening the file....')


#Raise Exception

#As a  python developer you can choose to throw an exception if condition occurs
#To throw (or raise) an exception , use 'raise' keyword

#Eample 10

# x=-1
#
# if x<0:
#     raise Exception('Sorry.. no numbers below zero')

#Example 11

# x='hello'
#
# if not type(x) is int:
#     raise TypeError('Only integers are allowed')
