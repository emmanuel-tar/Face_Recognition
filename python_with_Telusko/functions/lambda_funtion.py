from functools import reduce
#Lambda Function such as Fulter(),Nap(),Reduce()
#Using Function
def is_even(n):
    return n%2 ==0

def update(n):
    return n+2

def add_all(a,b):
    return a+b

nums = [3,2,6,8,4,2,9,7]

#Filter() by calling the created Function about
evens = list(filter(is_even,nums))

#Using Lambda
odd = list(filter(lambda n: n%2 !=0,nums))
double = list(map(lambda n: n*2,nums))
sum1 = reduce(lambda a,b,:a+b,double)


#USing Reduce()
sum = reduce(add_all,double)

print(double)
print(odd)
print(evens)
print('sum',sum)
print('Lambda Sum:',sum1)

#Using the Map() and Function

doubles = list(map(update,evens))
print(doubles)