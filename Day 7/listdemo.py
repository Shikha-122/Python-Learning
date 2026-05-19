#Creating list


# mylist1=[10,20,30,40]
# mylist2=['mango','guava','grapes']
# mylist3=[101,'John','A',True]
# mylist4=list()
#This will create empty list

# print(mylist1)
# print(mylist2)
# print(mylist3)

#Accessing items/value/object

# mylist=['apple','banana','cherry'] #index starts from 0
# print(mylist[0])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])

#Access multiple value  from the list [range of indexes]

# mylist=['apple','banana','cherry','Dragon Fruit','Orange','Grapes','Mango']
# print(mylist[2:5])#cherry,dragon fruit, Orange,Grapes
# print(mylist[-4:-1]) #Dragon Fruit, Orange, Grapes

#Change the value in list

# mylist=['apple', 'banana','cherry']
# print('Before the change:',mylist)
# print('Id before change', id(mylist))
# mylist[0]='aam'
# print('After the change:',mylist)
# print('Id after change', id(mylist))

#loop with list
# mylist=['apple', 'banana','cherry']
#
# for i in mylist:
#     print(i)

#Check if the item is exist or not
# mylist=['apple', 'banana','cherry']
#
# if 'bananaa'in mylist:
#     print('Yes, banana exist')
# else:
#     print('No, banana doesnot exist')

#Check the length of list

# mylist=['apple', 'banana','cherry']
# print(len(mylist))


#Count number of time a item repeated in a list.

# mylist=['apple', 'banana','apple','cherry', 'apple']
# print(mylist.count('apple'))

#Sorting the list
# mylist=['guava','pineapple','iceapple','dragonfruit','cherry','banana','apple']
# print('Orginal list',mylist)
# # mylist.sort() #Sorting in ascending order ['apple', 'banana', 'cherry', 'dragonfruit', 'guava', 'iceapple', 'pineapple']
# mylist.sort(reverse=True)
# print('Sorted List',mylist)

#Reversing the list items
#pre-requisite : Data must be in the sorted order.

# mylist=['apple', 'banana', 'cherry', 'dragonfruit', 'guava', 'iceapple', 'pineapple']
# print('Orginal list',mylist)
# mylist.reverse()
# print('Reverse value in a list',mylist)

#Append the value in a list
#New value added in the list.

# mylist=['apple', 'banana', 'cherry', 'dragonfruit', 'guava', 'iceapple', 'pineapple']
# print('Orginal list',mylist)
# mylist.append('mango')
# print('Updated list',mylist)

#Insertion
# mylist=['apple', 'banana', 'cherry', 'dragonfruit', 'guava', 'iceapple', 'pineapple']
# print('Before Insertion',mylist)
# mylist.insert(1,'berry')
# print('After Insertion',mylist)

#Methods to remove the elements from list
#Remove
# mylist=['apple', 'banana', 'cherry', 'dragonfruit', 'guava', 'iceapple', 'pineapple']
# print('Before Remove',mylist)
# mylist.remove('banana')
# print('After Remove',mylist)

#POP

# mylist=['apple', 'banana', 'cherry', 'dragonfruit', 'guava', 'iceapple', 'pineapple']
# print('Before Pop',mylist)
# mylist.pop(0)
# print('After Pop',mylist)

#Del
# mylist=['apple', 'banana', 'cherry', 'dragonfruit', 'guava', 'iceapple', 'pineapple']
# print('Before Del',mylist)
# del mylist[6]
# print('After Del',mylist)

#Deleting entire list

# mylist=['apple', 'banana', 'cherry', 'dragonfruit', 'guava', 'iceapple', 'pineapple']
# print('Before Del',mylist)
# del mylist

#Copying the list

#Approach 1 --- copy()

# mylist=['apple', 'banana', 'cherry']
# mylist2=mylist.copy()
# print(mylist)
# print(mylist2)

#Approach 2 -- list()
# mylist=['apple', 'banana', 'cherry']
# mylist2=list(mylist)
# print(mylist)
# print(mylist2)

#Join the list
# Approach 1 Using +

# mylist=['apple', 'banana', 'cherry']
# mylist1=['dragon fruit', 'grapes', 'pineapple']
# mylist2=mylist+mylist1
# print('Join List: ',mylist2)

#Approach 2 ... Using Loop
# mylist1=['apple', 'banana', 'cherry']
# mylist2=['dragon fruit', 'grapes', 'pineapple']
#
# for i in mylist2:
#     mylist1.append(i)
#
# print(mylist1)

#Approach 3--- Using extend()

# mylist1=['apple', 'banana', 'cherry']
# mylist2=['dragon fruit', 'grapes', 'pineapple']
#
# mylist1.extend(mylist2)
# print(mylist1)
