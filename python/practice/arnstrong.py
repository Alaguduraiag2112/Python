
for i in range(1001):
    num=i
    result=0
    l=len(str(i))
    while(i!=0):
        digit=i%10
        result+=digit**l
        i//=10
    if(num==result):
        print(num)