from array import *

arr = array('i',[])

n = int(input('Enter the length of the array: '))

for i in range(n):
    x = int(input('Enter the Next Value: '))
    arr.append(x)

print(arr)

val = int(input('Enter Value for Search: '))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k+=1
