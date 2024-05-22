from array import *

def count(lst):
    even = 0
    odd =0

    for i in lst:
        if i%2 ==0:
            even+=1
        else:
            odd+=1
    return even,odd







lst = array('i',[])

lst_len = int(input('Enter The Length Of Value: '))

for i in range(lst_len):
    lst_input = int(input('Enter Next Value: '))
    lst.append(lst_input)
    even,odd = count(lst)

print(lst)
print(even)
print(odd)
print('Even:{} and Odd: {}'.format(even,odd))


