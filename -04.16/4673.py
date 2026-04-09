M=[]
for i in range(1,10001):
    L=[]
    L.append(i)
    while i>0:
        L.append(i%10)
        i//=10
    M.append(sum(L))
for j in range(1,10001):
    if j in M:
        pass
    else:
        print(j)
