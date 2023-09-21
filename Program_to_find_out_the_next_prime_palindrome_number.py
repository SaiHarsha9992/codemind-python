def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True
def isPali(n):
    s = str(n)
    return s==s[::-1]
n = int(input())
n += 1
while True:
    if isPrime(n):
        if isPali(n):
            print(n)
            break
    n += 1
    
