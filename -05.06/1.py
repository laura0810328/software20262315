import random
n=int(input(""))
def makeMatrix(n):
    L=[[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            L[i].append(random.randint(1, n*n*10))
    return L

A,B=makeMatrix(n), makeMatrix(n)

def calculateMatrix(n):
    R=[[] for _ in range(n)]
    C=makeMatrix(n)
    value=0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                value+=A[i][k]*B[k][j]
            R[i].append(value)
            value=0
    
    for i in range(n):
        for j in range(n):
            R[i][j]+=C[i][j]
    return R,C

def f(x):
    for i in range(n):
        print(*x[i])
    print()


def printMatrix(n):
    X,Y=calculateMatrix(n)
    print("행렬 A")
    f(A)
    print("행렬 B")
    f(B)
    print("행렬 C")
    f(Y)
    print("행렬 A × B + C")
    f(X)
printMatrix(n)
