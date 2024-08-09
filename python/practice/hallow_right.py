n=int(input("enter the row number"))
for row in range(n):
    for col in range(n):
        if(col==0 or row==n-1 or row==col):
            print("*",end="")
        else:
            print(end=" ")
    print()

print("--------------------------------")

    # print hallow right angle in down
for row in range(n):
    for col in range(n):
        if(row==0 or col==n-1 or row==col):
            print("*",end="")
        else:
            print(end=" ")
    print()