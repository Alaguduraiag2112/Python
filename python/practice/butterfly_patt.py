
n=int(input("enter the number: "))
space=2*n-1
stars=0

# *       *
# **     **
# ***   ***
# **** ****
# **********
# **** ****
# ***   ***
# **     **
# *       *

for i in range(1,2*n):
    if(i<=n):
        space=space-2
        stars=stars+1
    else:
        space=space+2
        stars=stars-1
    # print(space)
    for j in range(0,stars):
        print("*",end='')
    for k in range(0,space):
        print(" ",end='')
    for j in range(0,stars):
        if(j!=n):
            print("*",end='')
    print()