num=7
sqr=num*num
s=str(sqr)
l=len(s)

mid=l//2
left=(int(s[:mid]))
right=(int(s[mid:]))
if(left+right==num):
    print("this karperker number")
else:
    print("this is not karperker number")
