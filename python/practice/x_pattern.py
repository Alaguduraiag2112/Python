n=int(input("enter the number: "))
str="program"
for i in range(n):
    for j in range(n):
        if j==i or j==n-i-1:
            print(str[j],end="")
        else:
            print(" ",end="")
    print()