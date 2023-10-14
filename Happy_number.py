n = int(input())
a = 0
while n:
    r = n%10
    a += pow(r,2)
    n //= 10
    if n == 0 and a < 10:
        if a == 7 or a == 1:
            print("True")
        else:
            print("False")
    elif n == 0 and a >= 10:
        n = a
        a = 0
        r = 0