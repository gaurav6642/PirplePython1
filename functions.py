Song="Hope"
Artist1="The Chainsmokers"
Artist2="Winona Oak"
Album="Sick Boy"
Genre="Rock"
YearofRelase=2019
DurationinMinutes=3.00 #DecimalVariable

#Funtion with return
def Songs(SongName):
    return SongName

def DurationofSong(Min):
    return Min

#Function without return
def Artist(Name1,Name2):
    print(Name1,Name2)

#Calling of Functions    
Songname=Songs(Song)
print(Songname)
time=DurationofSong(DurationinMinutes)
print(time)
Artist(Artist1,Artist2)