#Dictionaries are used to store data values in key: value pairs
#As of Python version 3.7, dictionaries are ordered . In python 3.6 and earlier , dictionaries are unordered.
#Dictionary items are ordered, changeable (mutable), and do not allow duplicates.
#Dictionary items are presented in key: value pairs, and cannot be referred to by using the key name.


#creating a dictionary

#approach 1:

#mydic={ 'brand':'ford','model': 'Aspire', 'year': 2024}

# mydic={ 'brand':'ford',
#         'model': 'Aspire',
#         'year': 2024
#       }
#
# print(mydic)

#approact 2 using dict() constructor

# mydict=dict( name='John', age=35, country='USA')
# print(mydict)

# Note:  one key can have multiple value

# mydict={ 'brand':'ford',
#          'model': 'Aspire',
#          'year': 2024,
#          'colours': ['red', 'blue', 'black', 'white'],
#          'brand':'hyundai'
#       }
# print(mydict)

#Accessing the value from the dictionary

#You can access the items of dictionary by referring its key name, inside[] brackets:

#Approach 1:

# mydict={ 'brand':'ford','model': 'Aspire', 'year': 2024}
#
# print(mydict['model'])

#Approach 2 : using get() method

# mydict={ 'brand':'ford','model': 'Aspire', 'year': 2024}
# print(mydict.get('brand'))

#Approach 3: Get Keys: keys() method will return a list of all the keys in the dictionary

# mydict={ 'brand':'ford','model': 'Aspire', 'year': 2024}
# print(mydict.keys())

#Approach 4: Get Values: values() method will return a list of all the keys in the dictionary

# mydict={ 'brand':'ford','model': 'Aspire', 'year': 2024}
# print(mydict.values())

#Approach 5: Get Items: items() method will return each item in a dictionary, as tuple in a list.

# mydict={ 'brand':'ford','model': 'Aspire', 'year': 2024}
# print(mydict.items())
# print(mydict)


#Check if key exists (searching key in dictionary)

# mydict={ 'brand':'ford','model': 'Aspire', 'year': 2024}
# if 'brand' in mydict:
#     print('Exists')
# else:
#     print('Not Exists')

#Adding items in dictionary

# mydic={'brand':'ford','model': 'Aspire', 'year': 2024}
# mydic['colour']='red'
# print(mydic)

#Updating dictionary -- update()

# mydic={'brand':'ford','model': 'Aspire', 'year': 2024}
# mydic['colour']='red'
# print('Before Updation:',mydic)
#
# mydic.update({'colour':'white' })
# mydic.update({'brand':'Hyundai' })
# print('After Updation:',mydic)


#Removing Items from the dictionary

#Approach1 : using pop()
# mydic={'brand':'ford','model': 'Aspire', 'year': 2024}
# print('Before Removal', mydic)
# mydic.pop('model')
# print('After Removal', mydic)

#Approach2 : using popitem()

#remove last inserted item (in version before 3.7 , a random item is removed)

# mydic={'brand':'ford','model': 'Aspire', 'year': 2024}
# print('Before Removal', mydic)
# mydic.popitem()
# print('After Removal', mydic)

#Approach3 : using del keyword -- removes the item with the specifed key name

#Example 1
# mydic={'brand':'ford','model': 'Aspire', 'year': 2024}
# print('Before Removal', mydic)
# #del mydic['model'] # this will remove only model item
# print('After Removal', mydic)

#Example 2
# mydic={'brand':'ford','model': 'Aspire', 'year': 2024}
# print('Before Removal', mydic)
# del mydic #delete dictionary completely
# print('After Removal', mydic) #Name Error:

#Approach 4 : The clear() method clears the dictionary
# mydic={'brand':'ford','model': 'Aspire', 'year': 2024}
# print('Before Removal', mydic)
# mydic.clear()
# print('After Removal', mydic)

#Copying the dictionary

#Approach 1: using copy()
# mydic1={'brand':'ford','model': 'Aspire', 'year': 2024}
# mydict2=mydic1.copy()
# print(mydic1)
# print(mydict2)

#Approach 2: using dict()

# mydic1={'brand':'ford','model': 'Aspire', 'year': 2024}
# mydic2=dict(mydic1)
# print(mydic1)
# print(mydic2)

#length of dictionary
# mydic1={'brand':'ford','model': 'Aspire', 'year': 2024}
# print(len(mydic1))

#looping with dictionary
#Print all the keys names in the dictionary , one by one

# mydic={'brand':'ford','model': 'Aspire', 'year': 2024}
# for x in mydic:
#     print(x)
#
# for x in mydic.keys():
#     print(x)

#Print all the values names in the dictionary , one by one
# mydic={'brand':'ford','model': 'Aspire', 'year': 2024}
#
# for x in mydic.values():
#     print(x)

#Print all the items in the dictionary , using loop

# mydic={'brand':'ford','model': 'Aspire', 'year': 2024}
#
# for x,y in mydic.items():
#     print(x,y)
