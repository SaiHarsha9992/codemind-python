n = int(input())
a = 0 
b = 1
c = a + b
while c < n:
    c = a + b
    if c < n:
        a = b
        b = c
print(c==n)