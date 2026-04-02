n=int(input())
L = list(map(int, input().split()))
L.sort()
sum=0
for i in range(n):
    sum+=L[i]*(2*i-n+1)*2
print(sum)
