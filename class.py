
class Vehicle: #__init__ method to set values
 def __init__(self,Make,Model,Year,Weight,NeedsMaintance=False,TripsSinceMaintenance=0):
  self.Make=Make
  self.c=0       #we use this as a flag in Switch method
  self.x=1000
  self.Model=Model
  self.Year=Year
  self.Weight=Weight
  self.NeedsMaintance=NeedsMaintance
  self.TripsSinceMaintenance=TripsSinceMaintenance
class Cars(Vehicle):
 def __init__(self,Make,Model,Year,Weight,NeedsMaintance,TripsSinceMaintenance,isDriving):
  Vehicle.__init__(self,Make,Model,Year,Weight,NeedsMaintance,TripsSinceMaintenance)
  self.isDriving=[]       # we are taking list 

 def Drive(self):
  self.isDriving.append(True)

 def Stop(self):
  self.isDriving.append(False)

 def Switch(self): # this method will going to check the Switching from true to false
  for i in self.isDriving:
   if i==True :
    self.c=1 
   if i==False and self.c==1:
    self.TripsSinceMaintenance=self.TripsSinceMaintenance+1
    self.c=0
  
 def Repair(self):
  if (self.TripsSinceMaintenance)>=100:
   self.TripsSinceMaintenance=0
   self.NeedsMaintance=False
   

d=Cars("Ford","Figo",2000,2009,False,98,"null")
e=Cars("Tata","Nano",1800,2011,True,97,"null")
f=Cars("Audi","A2",2500,2010,False,0,"null")

d.Stop()
d.Drive()
d.Drive()
d.Drive()
d.Stop()
d.Stop()
d.Drive()
d.Stop()
d.Switch()

e.Stop()
e.Drive()
e.Drive()
e.Drive()
e.Stop()
e.Switch()

f.Stop()
f.Drive()
f.Drive()
f.Drive()
f.Stop()
f.Switch()

d.Repair()

print("Make                  : "+d.Make)
print("Model                 : "+d.Model)
print("Year                  : "+str(d.Year))
print("Weight                : "+str(d.Weight))
print("TripsSinceMaintenance : "+str(d.TripsSinceMaintenance))
print("NeedsMaintance        : "+str(d.NeedsMaintance)+"\n")

print("Make                  : "+e.Make)
print("Model                 : "+e.Model)
print("Year                  : "+str(e.Year))
print("Weight                : "+str(e.Weight))
print("TripsSinceMaintenance : "+str(e.TripsSinceMaintenance))
print("NeedsMaintance        : "+str(e.NeedsMaintance)+"\n")

print("Make                  : "+f.Make)
print("Model                 : "+f.Model)
print("Year                  : "+str(f.Year))
print("Weight                : "+str(f.Weight))
print("TripsSinceMaintenance : "+str(f.TripsSinceMaintenance))
print("NeedsMaintance        : "+str(f.NeedsMaintance)+"\n")