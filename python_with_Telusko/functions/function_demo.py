

def greet():
    print('Hello,')
    print('Good Morning')

def add(x,y):
    c = x+y
    #print(c)
    return c



result = add(5,5)
print(result)
greet()


#---- Two Values return in function---
def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

result1,result2 = add_sub(45,90)
print(result1,'\n',result2)