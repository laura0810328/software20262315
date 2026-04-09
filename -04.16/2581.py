a = int(input())
b = int(input())
def f(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n%2==0:
        return False
    else:
        for i in range(3, n//2+1):
            if n%i==0:
                return False
            else:
                pass
        return True
L=[]

for j in range(a, b+1):
    if f(j)==True:
        L.append(j)
    else:
        pass
L.sort()
if len(L)==0:
    print(-1)
else:
    print(sum(L))
    print(L[0])
