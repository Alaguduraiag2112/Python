p=int(input("enter the number of rows for matrix 1: "))
q=int(input("enter the number of columns for matrix2: "))
n=int(input("enter the number of matrix1->column and matrix2->row: "))

matrix1=[[int(input()) for i in range(n)] for i in range(p)]
print("matrix1: ")
for i in range(p):
    for j in range(n):
        print(format(matrix1[i][j], "<3"),end=" ")
    print()

print("matrix2: ")
matrix2=[[int(input()) for i in range(q)] for j in range(n)]
print("matrix1")
for i in range(n):
    for j in range(q):
        print(format(matrix2[i][j], "<3"),end=" ")
    print()

print("matrix multiplication: ")
result=[[0 for i in range(n)] for j in range(n)]
for i in range(p):
    for j in range(q):
        for k in range(n):
            result[i][j]+=matrix1[i][k]*matrix2[k][j]

print(result)
