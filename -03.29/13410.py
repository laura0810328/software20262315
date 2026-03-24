m, n = map(int, input().split())
list=[]
for i in range(1, n+1):
    a=m*i
    a=int(str(a)[::-1])
    list.append(a)
print(max(list))
