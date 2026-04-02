n=int(input())
list=[]
sum=0
for i in range(n):
    a=int(input())
    if a!=0:
        list.append(a)
    else:
        del list[-1]
for j in range(len(list)):
    sum+=list[j]
print(sum)
