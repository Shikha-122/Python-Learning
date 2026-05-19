# 1. Arbitrary or Variable length arguments
# 2. Positional or Required Arguments
# 3. Keywords Arguments

#Example 1 Function with Arbitrary Arguments

# def sum_function(*numbers):
#     total=0
#     for i in numbers:
#         total+=i
#     return total
#
# print(sum_function(10,20,30,40,50))

#Example 1 (b)
# def mul_function(*numbers):
#     total=1
#     for i in numbers:
#         total*=i
#     return total
# print(mul_function(12,9))

# Example 2 Function with positional and keyword Arguments

# def myfun(i,j):
#     print(i,j)
#
# # myfun(3,2) #Positional Arguments
#
# myfun(i=20,j=30)  # Keyword Arguments
# myfun(j=20,i=30)  # Keyword Arguments


#Example 3 Default value can also be assigned to postitional arguments

# def myfun(i=100,j=100):
#     print(i,j)
#
# myfun(10)

#Example 4 : Mixing of both the positional and keyword arguments

# def myfun(a,b,c):
#     print(a,b,c)
#
# # myfun(10,20,30) #positional arguments
#
# # myfun(c=10,b=20,a=30) #keyword arguments
# # myfun(a=10,b=20,c=30)   #keyword arguments
#
# # myfun(10,20,c=30) #comb of positional and keyword arguments
# # myfun(10,b=20,c=30) #comb of positional and keyword arguments
#
# # myfun(a=10,20,30) #this is wrong because positional argument must appear before any keyword argument
#
# # myfun(10,30,b=20) # this is having error because b is assigning two times


#Example 5: Function can return multiple values

def largest(a,b):
    if a>b:
        return a,b
    else :
        return b,a

# print(largest(40,90))
res=largest(100,200)
print(res)
print(type(res))