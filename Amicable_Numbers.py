def fun(n):
    s = 0
    for i in range(1,(n//2)+1):
        if n%i == 0:
            s += i
    return s
a = int(input())
b = int(input())
c = fun(a)
d = fun(b)
if c == b and d == a:
    print("Amicable")
else:
    print("Not Amicable")