alpha={chr(i+65):i+1 for i in range(26)}
a="alagu".upper()
print(alpha)

sum=0
n=len(a)
for i in range(n):
    sum=sum+alpha[a[i]]
print(sum/len(a))
