n = int(input())
s = set()
for i in range(n):
    a, b = input().split()
    if b == "enter":
        s.add(a)
    else:
        s.remove(a)
for name in sorted(s, reverse=True):
    print(name)
