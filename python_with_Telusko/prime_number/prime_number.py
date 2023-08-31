num = int(input('Enter any Number: '))

for i in range(2,num):
    if num % i == 0:
        print('Not Prime')
        break

else:
    print('Prime')

    

