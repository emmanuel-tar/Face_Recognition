num = [25,12,36,95,14]
print (num[2:])
names = ['alvin','jake','paul',12]
print (names[:1])
mil = [num,names]
print (mil)
num.append(45)
num.clear
print(num)

#to insert element in the index number of the list
num.insert(2,77)
print(num)

#remove the element on the list
num.remove(12)
print(num)

#remove the last element on the list
num.pop()
print(num)

#delete multiple values in a list

del num[:2]
print(num)

# add multiple value in to the list

num.extend([29,87,55,110,43,38])
print(num)

#minimum and maximum value in  a list

print(min(num))

print(max(num))

print(sum(num))

#arrange element in a list

num.sort()
print(num)
