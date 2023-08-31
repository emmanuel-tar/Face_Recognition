from array import *

vals = array('i',[5,9,4,-3,6,2])

newArr = array(vals.typecode,(a*a for a in vals))

i=0

while i<len(newArr):
    print(newArr[i])
    i+=1

#for e in newArr:
    #print(e)
#vals.reverse()

#print(vals[0])

#for e in vals:
    #print(e)




