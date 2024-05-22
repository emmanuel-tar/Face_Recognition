
def person(name, **data):

    print('Name: ',name)
    

    for i,j in data.items():
        print(i,j)

person('Emmanuel',City = 'Lagos', Age = 32, Mobile = '09019404519')