
def person(name,age):
    print('Name: ',name,'\n','Age: ',age)

person('Emmanuel',32)


def sum(a,*b):
    c = a

    for i in b:
        c = c + i
    print(c)

sum(5,2,23,79)
