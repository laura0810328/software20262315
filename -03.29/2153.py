a=input()
n=0
for i in a:
    if i.islower():
        n+=ord(i)-ord('a')+1
    else:
        n+=ord(i)-ord('A')+27

def isPrime(n):
    if n < 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False   
    return True

if isPrime(n):
    print("It is a prime word.")
else:
    print("It is not a prime word.")
