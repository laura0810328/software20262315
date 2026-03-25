n = int(input())
original=n
count = 0
first=True

while n != original or first==True:
    n = (n % 10) * 10 + (n // 10 + (n % 10)) % 10
    count += 1
    first=False
print(count)
