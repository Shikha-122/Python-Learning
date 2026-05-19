#Global and Local Variables

#The variable create outside of the function are called as Global variable
#The variable create inside of the function are called as Local variable

#example 1
#
# x=20 # global variable.
#
# def myfun():
#     y=10  # local variable
#     print(x)  # able to access global variable within the function
#     print(y)
# myfun()
#
# print(x)
# print(y) # type error, cannot access local variable outside the function.

#Example 2 same name of local and global variable

# x=100
# def myfun():
#     x=200
#     print(x)
#
# myfun()
# print(x)

#Example 3 Modify global variable

# x=100
# def myfun():
#
#     global x
#     x=200
#     print(x)
#
# myfun()
# print(x)

#Example 4 Declare the global inside the function


def myfun():
     # global x=10  #SyntaxError: invalid syntax
     global x
     x=100
     print(x)

myfun()
print(x)
myfun()
