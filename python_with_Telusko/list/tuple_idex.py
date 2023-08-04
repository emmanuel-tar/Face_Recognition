#list is mutable and tuple is immutable i.e list value can be changed while tuple can't
tup = (21,3,56,90)
print (tup)

print(tup[1])

#add new value to index 1, error.....
#tup[1] = 24
#print (tup)

#SET, collection of unique element
s = {22,54,78,21,5,22}
print(s)

#set doesn't support indexing of elements or values.
s.add(68)
s.remove(22)
print(s)



#QUIZ QUESTION nums = [25,36,95,14,12,26] delete (95,14,12)
nums = [25,36,95,14,12,26]
del nums[2:4]
nums.sort()
print(nums)