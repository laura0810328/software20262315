a, b = map(int, input().split())
A = []
B = set()
for _ in range(a):
    A.append(input())
for _ in range(b):
    B.add(input())
result = []
for x in A:
    if x in B:
        result.append(x)
result.sort()
print(len(result))
for x in result:
    print(x)
