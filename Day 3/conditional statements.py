#if

#example 1 age>=18 eligible

#age=0
#if age>=18:
    #print('Eligible for Vote')

#Example 2 Check the amount value after discount

#amount=8000
#discount=0

#if amount>10000:
    #discount=amount*10/100

#print('Actual amount after reducing discount:',amount-discount)

#if else statements

#Example 1:

#age=20
#if age>=18:
 #   print("Eligible for vote")
#else:
    #print('Not eligible for vote')

#Example 2

# num=45
#
# if num%2==0:
#     print('Even Number is:',num)
#
# else:
#     print('Odd Number is:',num)

# if elif else

# Example 1
# Suppose there are different types of slabs of discoynt on a purchase
#20% on amount exceeding 10000,
#10% for amount between 5-10000
#5% if it is between 1 to 5000.
#no discount if amount <1000


# amount=11000
# discount=0
#
# if amount>10000:
#     discount=amount*20/100
# elif amount>5000:
#     discount=amount*10/100
# elif amount>1000:
#     discount=amount*5/100
# else:
#     discount=0
# print("Total amount after discount",amount-discount)

# Example 2 1-sunday, 2 monday

# weekno=7
#
# if weekno==1:
#     print("Sunday")
# elif weekno==2:
#     print('Monday')
# elif weekno==3:
#     print('Tuesday')
# elif weekno==4:
#     print('Wednesday')
# elif weekno==5:
#     print('Thrusday')
# elif weekno==6:
#     print('Friday')
# elif weekno == 7:
#     print('Saturday')
# else:
#     print("Invalid week number")

#nested-if-else
# num-- 2, 3
#num -- 2 but not 3
#num-- 3 but 2
#num --- not 2 not 3

# num=20
# print('Number:',num)
#
# if num%2==0:
#     if num%3==0:
#         print('Divisible by both 2 & 3')
#     else:
#         print('Divisible by 2 but not 3')
# else:
#     if num%3==0:
#         print('Divisible by 3 but not 2')
#     else:
#         print('Not Divisible by 2 and 3')

#And logical operator with if elif else
#find largest 3 numbers
#a>b and a>c a is largest
#b>a and b>c b is largest
#c is largest
# a=100
# b=20
# c=30
# if((a>b)and(a>c)):
#     print('A is largest',a)
# elif((b>a)and(b>c)):
#     print('B is largest', b)
# else:
#     print('C is largest', c)

