a, b = map(int, input().split())
if a > b:
    a, b = b, a
def f(x):
    return x * (x + 1) // 2 
print(f(b) - f(a - 1))
