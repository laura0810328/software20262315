a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
g, h = map(int, input().split())
list=[[a,c,e,g], [b,d,f,h]]
train=0
result =0
for i in range(4):
    train += list[1][i] - list[0][i]
    if train > result:
        result=train
print(result)
