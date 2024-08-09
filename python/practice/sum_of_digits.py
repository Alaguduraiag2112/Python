num=210
sum=0
while(num!=0):    # for i in range(len(str(num)))
    rem=num%10
    sum+=rem
    num//=10
print(sum)