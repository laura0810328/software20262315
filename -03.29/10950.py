n=int(input())
list=[]
for i in range(n):
    x,y=map(int, input().split())
    list.append(x)
    list.append(y)

for j in range(n):
    print(list[j*2]+list[j*2+1])
