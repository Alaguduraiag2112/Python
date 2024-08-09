# li=[3,2,[1,5,6],8,[9,10],6]

# duplicate index
# li=[3,2,1,1,5,6,8,6,6]
# lis=[x for x in range(len(li)) if li[x]==6]
# print(lis)


list1=[]
def max_min(li):
    for x in li:
        if type(x)==list:
            max_min(x)
        else:
            list1.append(x)
    return min(list1)

#find max and min
li=[2,1,[9,7,0],2,8,4]
print(max_min(li))