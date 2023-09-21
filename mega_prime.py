def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True
n = int(input())
if isPrime(n):
    c = 0
    nd = len(str(n))
    t = n
    while t!=0:
        r = t%10
        if isPrime(r):
            c += 1
        t //=10
    if (c == nd):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")