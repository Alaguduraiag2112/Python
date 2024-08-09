# for i in range(1,2):
#     print(i)

# 1  
# 1 2  
# 1 2 3  
# 1 2 3 4  
# 1 2 3 4 5 

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")

print("-----------------------------------------------")

# floyd triangle

# 1  
# 2 3  
# 4 5 6  
# 7 8 9 10  
# 11 12 13 14 15

num=1
for i in range(1,6):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print(" ")

print("----------------------------------------")

# print python instead of stars

# p
# p y
# p y t
# p y t h
# p y t h o
# p y t h o n

st="python"
for i in range(0,6):
    for j in range(0,i+1):
        print(st[j],end=" ")
    print(" ")