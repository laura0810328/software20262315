list=[]
n=int(input())
for i in range(n):
    a=int(input())
    list.append(a)
list.sort()
for j in range(n):
    print(list[j])
