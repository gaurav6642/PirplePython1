var1=1
var2=1
var3=3
var4=2

def equals(v1,v2,v3):
    if v1==v2 or v1==v3 or v2==v3:
      return True
    else:
      return False

ans=equals(var1,var2,var3)#two values are equal
print(ans)

ans=equals(var1,var4,var3)#all the three values are different
print(ans)