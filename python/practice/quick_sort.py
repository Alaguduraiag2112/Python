# n=int(input("enter the number of elements: "))
# li=[int(input()) for x in range(n)]

def pivot_place(li,first,last):
    pivot=li[first]
    left=first+1
    right=last
    while True:
        while left<=right and li[left]<=pivot:
            left+=1
        while left<=right and li[right]>=pivot:
            right-=1
        if right<left:
            break
        else:
            li[left],li[right] = li[right],li[left]
    li[first],li[right]=li[right],li[first]
    return right

def quicksort(li,first,last):
    if(first<last):
        p=pivot_place(li,first,last)
        quicksort(li,first,p-1)
        quicksort(li,p+1,last)

li=[8,3,4,10,11,9]

first=0
last=len(li)-1
quicksort(li,first,last)
print(li)