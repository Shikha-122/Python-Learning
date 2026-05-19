# str='hello Python'
# print(len(str))
#
# mylst=[10,20,30,40,50]
# print(len(mylst))
#
# mytup=(1,2,3,4,5,6,7,8)
# print(len(mytup))
#
# dict={'id':134,
#        'name':'shikha'
#       }
# print(len(dict))

#Example 1 for method overloading (Polymorphism)

# class Human:
#     def sayHello(self,name=None):
#         if name is not None:
#             print('Hello',name)
#         else:
#             print('Hello')
#
# h=Human()
# h.sayHello()
# h.sayHello('John')

#Example 2:

# class Calculation:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
#
# cal=Calculation()
# # cal.add(10,20,30)
# cal.add()
# cal.add(10,20)
