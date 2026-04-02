list=[]
count=1
for i in range(10):
    a=int(input())
    b=a%42
    list.append(b)
list.sort()
for j in range(9):
    if list[j]==list[j+1]:
        pass
    else:
        count+=1
print(count)
