#Mutability vs Immuntability

#Mutable object:  Can be changed after creation (eg list, dict,set)
#Immutable Object:  Cannot be changed after creation (eg int, float, tuple, str etc)

#example1

# str='hello'
# print('Orginal String: ',str)
# print('Address:',id(str))
#
# # print(str[0])
#
# #str[0]='H' #String is immutable we cannot change the value
#
# str='H'+str[1:]
# print(str)
# print(id(str))

#Example 2

# s1='python'
# print(id(s1))
# s1= s1.replace('p','P')
# print(id(s1))

#Example 3

mylist=['h','e','l','l','o']
print('Orginal List:',mylist)
print('Before Change ID:',id(mylist))
mylist[0]='H'
print('Changed list',mylist)
print('After Change ID:',id(mylist))
