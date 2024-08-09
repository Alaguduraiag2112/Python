
def isHappy(n):
    res=sum=0
    while(n>0):
        res=n%10
        sum=sum+(res*res)
        n=n//10
    return sum

n=17
result=n

while result!=1 and result!=4:
    result=isHappy(result)

if result==1:
    print("happy number: ",n)
elif result==4:
    print("unhappy number: ",n)