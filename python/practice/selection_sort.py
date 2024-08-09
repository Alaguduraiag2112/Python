
li=[2,1,4,1001,3,11,10]
for i in range(len(li)-1):
    min=i
    for j in range(i+1,len(li)):
        if(li[j]<li[min]):
            min=j
    if(li[min]!=li[i]):
        li[min],li[i]=li[i],li[min]
print(li)


# n=int(input("enter the numbers: "))
# li=[int(input()) for i in range(n)]









li=[3,2,1,9,8,7]

for i in range(len(li)-1):
    for j in range(len(li)-1-i):
        if(li[j]>li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]
   
print(li)