# x=8
# r= x % 2
# if r==0:
#     print('Even Number')
#
# else:
#     print('Odd Number')
#
#
#
# print('bye')
# x=int(input("Enter any number from 1 -  4: "))

# if x==1:
#     print('One')
# elif x==2:
#     print('Two')
#
# elif x==3:
#     print('Three')
#
# elif x==4:
#     print('Four')
#
# else:
#     print('Wrong Input')

    #1. write a code to check given
    # number is positive or negative

    # 2. take three values from user and
    # find the greatest number from them

    # solution

# num = int(input('Enter any number: '))
# if num >=0:
#
#     if num == 0:
#         print('Zero')
#     else:
#         print('Positive Number')
# else:
#     print('Negative Number')



# Solution#2

num1 = int(input('Enter First Number: '))
num2 = int(input('Enter Second Number: '))
num3 = int(input('Enter Third Number: '))

if(num1 >=num2) and (num1>=num3):
    largest =num1
elif(num2>=num1) and (num2>=num3):
    largest = num2
else:
    largest =num3

print('The largest value is: ', largest)