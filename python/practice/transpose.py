n=int(input("enter the number of row: "))
m=int(input("enter the number of columns: "))

matrix1=[[int(input()) for i in range(m)] for j in range(n)]
result=[[0 for i in range(n)] for j in range(m)]
print("matrix1: ")
for i in range(n):
    for j in range(m):
        print(format(matrix1[i][j], "<3"),end=" ")
    print()

for i in range(m):
    for j in range(n):
        result[i][j]=matrix1[j][i]
print(result)