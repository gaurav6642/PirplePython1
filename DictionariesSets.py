FavSong={'Song':'Hope','Artist1':'The Chainsmokers','Artist2':'Winona Oak','Album':'Sick Boy','Genre':'Rock','YearofRelase':'2019','DurationinMinutes':'3.00'}
for i in FavSong:
 print (i,"=>",FavSong[i]) #FavSong[i]




def Guess(key,val):
 for i in FavSong:
  if i==key and FavSong[i]==val:
   return True
 return False

K=input("Guess Key Name: (like Song,Album,YearOfRelase)\n")#taking key
V=input("Guess Key's Value:\n")#taking value
g=Guess(K,V)

print(g)
 
 