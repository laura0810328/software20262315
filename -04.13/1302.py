n = int(input())
list = []
for i in range(n):
    list.append(input())
list.sort()

max = 1
count = 1
result = list[0]
for j in range(1, n):
    if list[j] == list[j-1]:
        count += 1
    else:
        count = 1
    if count > max:
        max = count
        result = list[j]
print(result)
