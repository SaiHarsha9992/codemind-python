def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True
a = int(input())
b = int(input())
c = a+b
t = c
t += 1
while True:
    if isPrime(t):
        s = t
        break
    t += 1
print(s-c)