#concatenation +

#Case 1 : when we use + between 2 numeric values, it will perform addition
print(10+10)  #20 valid
print(10.5+12.0) #22.5 valid
print(10+10.5) #20.5 valid

#Case 2 : when we use + between strings, it will perform concatenation
print('welcome ' + 'python')

#Case 3 : when we use + between one boolean and numeric then also perform addition operation
print(True+5) #True=1
print(False+5) #False=0

print(True+True) #2

#Case 4 We cannot concatenate 2 different types

print(10+'hi') # not valid becoz 2 values are different type
print(10.5+'hi') # not valid becoz 2 values are different type
print(True+'welcome') # not valid becoz 2 values are different type