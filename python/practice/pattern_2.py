num=int(input("enter the number: "))
for i in range(num):
    for j in range(1,num-i+1):
        print(format(" ","<4"),end=" ")
    for j in range(i,0,-1):
        print(format(j,"<4"),end=" ")
    for j in range(2,i+1):
        print(format(j,"<4"),end=" ")
    print()
