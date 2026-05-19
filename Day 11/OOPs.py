#Example 1 : Creating a class along with object

# class Myclass:
#     def myfun(self):
#      pass
#
#     def display(self,name):
#      print (name)
#
# mc1=Myclass()
# mc1.myfun()
# mc1.display('shikha')
#
# mc2=Myclass()
# mc2.myfun()
# mc2.display('prabhat')

#Example 2 : Instance vs static method
#Note: 'self' inside the static method is just a parameter name, it doesnot refer to objects

# class Myclass():
#     def m1(self):
#         print('This is instance method')
#
#     @staticmethod
#     def m2(self,num):
#         print(self,num)

# mc=Myclass() #Object Creation.
# mc.m1()
# mc.m2(10,20)

# Myclass.m2(10,20)  # static methods can be access directly from the class
# Myclass.m1()

#Example 3: define the variables inside the class (class variables/instance variables)

# class Myclass:
#     a=10
#     b=30
#     def add(self):
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
#
# mc=Myclass()
# mc.add()
# mc.mul()

#Example 4 Local Variables, Global Variables, Class Variables

# i,j=10,15  # Global Variables
#
# class Myclass:
#     a,b=20,25  # Class Variables
#
#     def add(self,x,y):
#         print(x+y)  # Local Variables
#         print(self.a+self.b) # Class Variables
#         print(i+j) # Global Variables
#
# mc=Myclass()
# mc.add(10,20)

# Example 5 Local Variables, Global Variables, Class Variables (names of variables are same)

# a,b=10,15  # Global Variables
#
# class Myclass:
#     a,b=20,25  # Class Variables
#
#     def add(self,a,b):
#         print(a+b)  # Local Variables
#         print(self.a+self.b) # Class Variables
#         print(globals()['a']+globals()['b']) # Global Variables
#
# mc=Myclass()
# mc.add(10,20)

# Class with constructor
# __init__(self) : constructor
# constructor used for initilize data
# constructor invoked automatically when object is created.

#Example 6
# class Myclass:
#     def __init__(self):
#         print('This is constructor.....')
#     def m1(self):
#         print('Hello Python....')
#     def m2(self,x,y):
#         return x+y
#
# mc=Myclass()
# mc.m1()
# print(mc.m2(10,20))

#Example 7 : Constructor with parameter and class variable

# class Myclass:
#     name='John' #Class Variable
#     def __init__(self,name):
#         print(name)
#         print(self.name)
#
#
# mc=Myclass('Kelvin')

#Example 8: A class with constructor and methods

class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def display(self):
        print(self.eid,self.ename,self.sal)

e1=Emp(101,'Shikha',60000)
e1.display()

e2=Emp(102,'Prabhat',70000)
e2.display()








