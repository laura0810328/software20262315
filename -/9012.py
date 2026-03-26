n = int(input())

for _ in range(n):
    word = input()
    count = 0
    
    for w in word:
        if w == '(':
            count += 1
        else:
            count -= 1
        
        if count < 0:
            break
    
    if count == 0:
        print("YES")
    else:
        print("NO")
