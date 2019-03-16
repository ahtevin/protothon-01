
def caps(x):
     y=x.upper()
     print(y)
def lower(x):
     y=x.lower()
     print(y) 
def title(x):
     y=x.title() 
     print(y)
def letter(x): 
     y=x.cap()
     print(y)            
x=input("enter the word")
print("1 for upper")
print("2 for lower")
print("3 for title")
print("4 for start")
type=int(input("Enter the type conversion"))
if(type==1):
     caps(x)
elif(type==2):
     lower(x)
elif(type==3):
     title(x)
elif(type==4):
     letter(x)   



   