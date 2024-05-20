from numpy import *
#------------- Using linspace
#arr = linspace(0,16,2)
#--------------------------

#-------Using logspace____
arr = logspace(1,40,5)
print(arr)

#-------- zeros - and ones ----------

arr1 = ones(5,int)
print(arr1)

#------Copy from existing Array

arr2 = array([1,2,3,4,5,6])
arr2 = arr2 +5

arr3 = array([3,7,8,2,1,4])

res = arr2+arr3
print(arr3)
print(arr2)
print('Result Sine: ',sin(res))
print('Result Cosine: ',cos(res))
print('Result Tangent : ',tan(res))
print('Result: ',log(res))
print('Result Sqaure root: ',sqrt(res))

# concatenate array----
print(concatenate([arr3,arr2,arr1]))


#-----Copy From Existing Array
arr2=arr3
print(arr2)
print(arr3)
arr3 = arr2.copy()
print(id(arr2))
print(id(arr3))
