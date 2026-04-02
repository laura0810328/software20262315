n = int(input())
list=[]
for i in range(n):
    test = input()
    score = 0
    total = 0
    for j in test:
        if j == "O":
            score += 1
            total += score
        else:
            score = 0
    list.append(total)
for k in range(n):
    print(list[k])
