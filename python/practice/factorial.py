n=int(input("enter the number to factorial"))
fact=1

# for i in range(n,0,-1):
#     print(i)

# iterative method to find factorial of given number
for i in range(1,n+1):
    fact*=i
print(fact)
