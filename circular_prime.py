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
s = str(n)
s = s[::-1]
rn = int(s)
if(isPrime(n) and isPrime(rn)):
    print("circular prime")
elif isPrime(n) and (not isPrime(rn)):
    print("prime but not a circular prime")
else:
    print("not prime")