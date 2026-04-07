n = int(input())
L = list(map(int, input().split()))
count = {}
for i in L:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
m = int(input())
M = list(map(int, input().split()))
N = []
for j in range(len(M)):
    if M[j] in count:
        N.append(count[M[j]])
    else:
        N.append(0)
print(*N)
