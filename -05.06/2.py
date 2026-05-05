import random
n=int(input(""))
def makeMatrix(n):
    L=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            L[i].append(random.randint(1, n*n*10))
    return L

X=makeMatrix(n)
def transposedMatrix(n):
    Y=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            Y[i].append(X[j][i])
    return(Y)

def printMatrix(n):
    print("행렬 A")
    for i in range(n):
        print(*X[i])
    print()
    print("행렬 A의 전치행렬")
    Y=transposedMatrix(n)
    for i in range(n):
        print(*Y[i])
printMatrix(n)
