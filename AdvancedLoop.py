r=0
c=0
def board(r,c):
 if r<=21 and c<=67:
  r=r*2
  c=c*2
  for row in range(r):
   if row%2==0:
    for col in range(1,c):
     if col%2==1:
      if col!=c-1:
       print(" ",end="")
      else:
       print(" ")
     else:
      print("|",end="")
  
   else:
    print("-"*col)
 else:
  print("False")

board(3,7)
board(9,10)
board(21,68)#not fitting screen size so it print false