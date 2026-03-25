a=int(input())
for i in range(a):
    if a%2==0:
        print("* "*(a//2))
        print(" *"*(a//2))
    else:
        b=(a+1)//2
        print("* "*(b))
        print(" *"*(b-1))
