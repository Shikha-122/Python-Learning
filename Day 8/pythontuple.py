#Creating a tuple

# mytuple=('apple', 'banana','cherry')
# print(mytuple)

#Accessing tuple elements/values
#
# mytuple=('apple', 'banana','cherry')
# print(mytuple[0])
# print(mytuple[-1])

#Count number of times items is repeated

# mytuple=('apple', 'banana','apple','cherry','apple')
# print(mytuple.count('apple'))
#
# #Ranges of indexes
#
# mytuple=('apple', 'banana','cherry','dragonfruit','pineapple','rasberry', 'mulberry')
# print(mytuple[2:5]) #('cherry','dragonfruit','pineapple')
# print(mytuple[-4:-1]) # ('dragonfruit','pineapple','rasberry')

#Change the value in the tuple
#by default tuple doesnot allow you to change because it is immutable
#by there is work around

#tuple-->list--->tuple

# mytuple=('apple', 'banana','cherry')
# mylist=list(mytuple)
# print('After converting into the list',mylist)
# mylist[1]='orange'
# print('After changing mylist is',mylist)
# mytuple=tuple(mylist)
# print(mytuple)

#retrive the data from loop

# mytuple=('apple', 'banana','cherry')
# for i in mytuple:
#     print(i)

#item exists in the tuple:

# mytuple=('apple', 'banana','cherry')
#
# if 'banana' in mytuple:
#     print('Item exist in mytuple')
# else:
#     print('Item doesnot exist in mytuple')

#length- count number of value in a tuple

# mytuple=('apple', 'banana','cherry')
# print(len(mytuple))

#Copy()

# mytuple=('apple', 'banana','cherry')
# mytuple1=mytuple
# print(mytuple)
# print(mytuple1)


#Remove the value from the tuple --   not possible because tuple is immutable
mytuple1=('apple', 'banana','cherry')
mytuple2= ('dragonfruit', 'elderberry', 'flat peach')

mytuple3= mytuple1+mytuple2

print(mytuple3)





