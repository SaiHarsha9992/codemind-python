n = int(input())
a = 0
b = 1
c = a+b
print(0, 1, end = ' ')
for i in range(2,n):
    c = a + b
    a = b 
    b = c
    print(c, end = ' ')
    