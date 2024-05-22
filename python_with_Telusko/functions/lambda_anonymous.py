

def square(a):
    return a*a


result = square(5)
print(result)
# end def

#--------------------
#Use a Lambda Function
#--------------------

f = lambda a: a*a
result = f(12)
print(result)

#Passing two Objects

j= lambda a,x: a/x
result = j(24,4)
print(result)