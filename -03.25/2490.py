list=[[],[],[]]
list2=["E", "A", "B", "C", "D"]
list3=[]
for x in range(3):
    a,b,c,d=input().split()
    list[x].append(int(a))
    list[x].append(int(b))
    list[x].append(int(c))
    list[x].append(int(d))
    list[x].sort()
for j in range(3):
    t=0
    for k in range(4):
        if list[j][k]==0:
            t=(k+1)%5
    list3.append(t)
for y in range(3):
    print(list2[list3[y]])
