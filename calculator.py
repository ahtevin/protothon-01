def add():
    x=float(input("Enter the value for x"))
    y=float(input("Enter the value for y"))
  
    c=x+y
    print("the sum is:",c)

def sub():
    x=float(input("Enter the value for x"))
    y=float(input("Enter the value for y"))
    c=x-y	
    print("The diff is :",c)

def mul():
    x=float(input("Enter the value for x"))
    y=float(input("Enter the value for y"))
    c=x*y
    print("the val is:",c)

def div():
    x=float(input("Enter the value for x"))
    y=float(input("Enter the value for y"))
    if(y==0):
         print("invalid number, please enter valid number")
    c=x/y
    print("the val is:",c)
print("enter 1 for add")
print("enter 2 for sub")
print("enter 3 for mul")
print("enter 4 for div")
val=int(input("Enter the operation"))
if(val==1):
  add()
elif(val==2):
    sub()
elif(val==3):
   mul()
elif(val==4):
   div()
else:
   print("Please enter the correction option")                    
