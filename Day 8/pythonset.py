#Creating Sets

# set1={10,20,30,40,50}
# set2={'Rohan','Mohan','Sohan'}
# set3={10,'Max','SDET',60000}
#set4=set()
#
# print(set1)
# print(set2)
# print(set3)
#print(set4)

#Access the value from the set
#You cannot access items in a set by referring to an index(becoz set doesnot support index)

#You cannot change the items, but you can add new items to set(becoz set doesnot support index)

#Access data from the set using for loop

# myset={'Apple', 'Mango', 'Guvava'}
#
# for i in myset:
#     print(i)

#Check if the value exisit in the set (searching the value/item in the set)

# myset={'apple','berry','cherry'}

# if 'apple' in myset:
#     print('Items exist in the list')
# else:
#     print('Items doesnot exist in the list')

#Find the length / number of values in a set
# myset={'apple','berry','cherry'}
# print(len(myset))

#count number of times value is repeated in the set
#Not possible , since set doesnot allowed duplicate

#sorting the set
#Not possible , since set is unordered

#reversing the set
#Not possible , since set is unordered


#Add items/ value into the set
# myset={'apple','berry','cherry'}
# print('Before Addition', myset)
# myset.add('dragon-fruit')
# print('After Addition', myset)

#update
# myset={'apple','berry','cherry'}
# print('Before Updation', myset)
# myset.update(['Dragon-fruit','kiwi','mul-berry'])
# print('After Updation', myset)

#if you have duplicate value in a set

# myset={1,2,3,4,5,6,1,2,3,4,5,6} #duplicate value will be ignore
# print(myset)

#Remove items/values from the set

#Approach 1: Using removal()

# myset={'apple','berry','cherry'}
# print('Before removal',myset)
# myset.remove('apple')
# myset.remove('xyx') #Key Error : if the value is not exist in the set
# print('After removal', myset)

#Approach 2: using discard()

# myset={'apple','berry','cherry'}
# print('Before discard',myset)
# myset.discard('apple')
# myset.discard('xyx') # No Key Error if value is not present in the set
# print('After discard', myset)

#Approach 3: using popup()

# myset={'apple','berry','cherry'}
# print('Before pop',myset)
# myset.pop()
# print('After pop',myset)

# clearing values from the set

# myset={'apple','berry','cherry'}
# myset.clear()
# print('After clearing: ',myset)

#delting set

# del myset
# print ('After deleting:', myset) #NameError


#copying set

#Approach 1 copy()

# myset1={'apple','banana', 'cherry'}
# myset2=myset1.copy()
# print(myset1)
# print(myset2)


#Approach 2 : set()

# myset1={'apple','banana', 'cherry'}
# #myset2=myset1
# #myset2=set(myset1)
#
# print(myset1)
# print(myset2)

#Joining of set

#Approach 1 : using union()

# myset1={'a','b','c'}
# myset2={10,20,30}
#
# myset3=myset1.union(myset2)
# print(myset3)

#Approach 2: using | symbol
# myset1={'a','b','c'}
# myset2={10,20,30}
#
# myset3=myset1 | myset2
# print(myset3)

#Intersection - Retriving common value from two set
# Approach 1 -- intersection()
# myset1={'a','b','c',1}
# myset2={2,3,'s'}
# myset3=myset1.intersection(myset2)
# print(myset3)

#Approach 2 -- using & symbol

myset1={'a','b','c',10}
myset2={10,20,30,'a'}

myset3=myset1 & myset2
print(myset3)


