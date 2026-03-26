list=[]
for i in range(9):
    s=int(input())
    list.append(s)
    if max(list)==s:
        k=i+1
print(max(list))
print(k)
