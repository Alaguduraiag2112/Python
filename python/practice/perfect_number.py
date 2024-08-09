n=int(input("enter the number: "))
result=0
for i in range(1,n):
    if(n%i==0):
        result+=i
if(result==n):
    print(n,"this is perfect number")
else:
    print(n,"this is not perfect number")

#write program for cetain number series

n=int(input("enter the numbers: "))
li=[int(input() for i in range(n))]