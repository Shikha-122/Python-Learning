# Example 1

# class A:
#     def m1(self):
#         print('This is m1 method from class A ')
#
# class B(A):
#     def m2(self):
#         print('This is m2 method from class B')
#
# bobj=B()
# bobj.m1()
# bobj.m2()


#Example 2: single inheritance

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=400,200
#     def m2(self):
#         print(self.a-self.b)
#
# bobj=B()
# bobj.m1()
# bobj.m2()

# Example 3 : Multi level Inheritance

# class A:
#     x,y=100,200
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j=12,5
#     def m3(self):
#         print(self.i * self.j)
# mango=C()
# mango.m3()
# mango.m2()
# mango.m1()

#Example 4 : Hierachy Inheritance

# class A:
#     x,y=100,200
#     def m1(self):
#         print(self.x + self.y)
#
# class B(A):
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j=12,5
#     def m3(self):
#         print(self.i * self.j)
#
#
# boj=B()
# boj.m1()
# boj.m2()
#
# cat=C()
# cat.m1()
# cat.m3()


# Example 5 : Multiple Inheritance

# class A:
#     x,y=100,200
#     def m1(self):
#         print(self.x + self.y)
#
# class B:
#     a,b=200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j=12,5
#     def m3(self):
#         print(self.i * self.j)
# mango=C()
# mango.m1()
# mango.m2()
# mango.m3()

#Example 6 : Calling parent class method using child class (super())

# class A:
#     def m1(self):
#         print('This is m1 method from class A')
#
# class B(A):
#     def m1(self):
#         print('This is m1 method from Class B')
#         super().m1() #invoke the immediate the parent class method
#
# boy=B()
# boy.m1()

#Example 7 Calling parent class variable using child class

# class A:
#     a,b=10,20
#
# class B(A):
#     i,j=30,20
#
#     def m1(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         print(self.a+self.b)
#
# bob=B()
# bob.m1(1000,2000)

#Example 8 : Overridding Variables


# class Parent:
#     name='Scott'
# class Child(Parent):
#     name='John'
#     def m(self):
#         print(super().name)
#
# ch=Child()
# print(ch.name)
# ch.m()

#Example 9: Overriding methods

# class Bank:
#     def rateofinterset(self):
#         return 0
#
# class XBank(Bank):
#     def rateofinterset(self):
#         return 10.5
#
# class YBank(Bank):
#     def rateofinterset(self):
#         return 12
#
# x=XBank()
# print(x.rateofinterset())
#
# y=YBank()
# print(y.rateofinterset())

