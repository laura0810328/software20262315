n=int(input())
list2=[]
for i in range(n):
    count=0
    sum=0
    list1 = list(map(int, input().split()))
    for j in range(1, len(list1)):
        sum+=list1[j]
    a=sum/list1[0]
    for k in list1[1:]:
        if a<k:
            count+=1
    list2.append(count/list1[0]*100)
    list1.clear()
for t in range(len(list2)):
    print(f"{list2[t]:.3f}","%",sep="")
