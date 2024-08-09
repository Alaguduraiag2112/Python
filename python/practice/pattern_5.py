
# 1
# 2 6
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

# n=int(input("enter the number: "))
# for row in range(n):
#     val=row+1
#     dec=n-1
#     for col in range(row+1):
#         print(val,end=" ")
#         val+=dec
#         dec-=1
#     print()


# 15         example n=5---> 1+2+3+4+5=15  --->n*(n+1)//2
# 14 10      k-row and then inner iteration print it first and then decrese by n-1,n-2 and n-3 so on
# 13 9 6 
# 12 8 5 3 
# 11 7 4 2 1 


def num(n):
    return n*(n+1)//2

n=int(input("enter the number: "))
k=num(n)
for row in range(n):
    val=k-row
    dec=n-1
    for col in range(row+1):
        print(val,end=" ")
        val-=dec
        dec-=1
    print()