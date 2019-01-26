import os;
fname = input("Enter file name: ")
print(fname)

if os.path.isfile(fname):
 choice=input("A) Read the file\nB) Delete the file and start over\nC) Append the file\nD) Replace a single line\n")
 if choice=="A":
   fptr=open(fname,"r")
   print(fptr.read())
   fptr.close()
 elif choice=="B":
   fptr=open(fname,"w")
   text=input("write in a file : \n")
   fptr.write(text)
   fptr.close()
 elif choice=="C":
   fptr=open(fname,"a")
   text=input("Append a file : \n")
   fptr.write(text)
   fptr.close()
 else :
   print("wrong input..")
   
 
 
else:
 fptr=open(fname,"w")
 text=input("write in a file : \n")
 fptr.write(text)
 fptr=open(fname,"r")
 print (fptr.read())
 fptr.close() 

