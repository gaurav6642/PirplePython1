myUniqueList=[]

def addDatatoList(val):
 if val in myUniqueList:
    return False
 else:
    myUniqueList.append(val)
    return True

check=addDatatoList(1)
print(check)

check=addDatatoList(2)
print(check)

check=addDatatoList("hello")
print(check)

check=addDatatoList(1)#it will return false because 1 is already in list
print(check)

print(myUniqueList)


