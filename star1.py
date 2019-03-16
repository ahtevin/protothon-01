#def star(n):
value=int(input("Enter the no of rows "))   
x=[]
for i in range(value):
    x.append([])
    x[i].append(5)
    for j in range(1,i):
        x[i].append(x[i-1][j-1]+x[i-1][j])
    if(value!=0):
        x[i].append(10)
for i in range(value):
    print("   "*(value-i),end="",sep="")
    for j in range(0,i+1):
        print('{0:6}'.format(x[i][j]),end="",sep="")
    print()

 