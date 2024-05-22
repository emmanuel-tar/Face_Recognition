
def div(a,b):
    print(a/b)
    

# what if the numerator is less than the denominator
#creating a new function
def smart_div(funct):
    
    def inner(a,b):
        if a<b:
            a,b=b,a
        return funct(a,b)
    return inner


div = smart_div(div)

div(2,4)