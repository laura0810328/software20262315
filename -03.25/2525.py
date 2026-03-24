a,b=input().split()
c=int(input())
a=int(a)
b=int(b)
if b+c>=60:
    d=(b+c)%60
    a+=(b+c)//60
else:
    d=b+c
    a+=(b+c)//60
if a>=24:
    a=a%24
print(a, d)
