m = int(input())
sum=99
def countNumber(m):
    L=[]
    count=0
    while m>0:
        L.append(m%10)
        m//=10
    TF(L)
    if TF(L)==True:
        count+=1
    else:
        pass

    return count

def TF(L):
    for i in range(1, len(L)-1):
        if L[i] - L[i-1]==L[i+1] - L[i]:
            pass
        else:
            return False
    return True

if m<100:
    print(m)
else:
    for j in range(100, m+1):
        sum+=countNumber(j)
    print(sum)
