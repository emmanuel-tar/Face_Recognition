from numpy import *
# Multi-dimensioanl array---

arr1 = array([
    [1,2,3],
    [4,5,6],
    [9,7,10]

])
arr2 = arr1.flatten()
print(arr1.size)
print(arr1.dtype)
print(arr1.ndim)

print(arr2)

m =matrix(arr2)
m2 = matrix('34,2,7;2,8,9;3,5,6')

print(diagonal(m2))
print(m2)
print('shape: ',m.reshape(3,3))
print('minimum: ',m2.min())
print('maximum: ',m2.max())

m3 = m.reshape(3,3) + m2;
m4 =m.reshape(3,3) * m2
print('Addition: \n',m3)
print('Multiplication: \n',m4)
