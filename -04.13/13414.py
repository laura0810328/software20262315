import sys
input = sys.stdin.readline
m, n = map(int, input().split())
d = {}
for i in range(n):
    a = input().strip()
    d[a] = i  
L = sorted(d, key=d.get)
print('\n'.join(L[:m]))
