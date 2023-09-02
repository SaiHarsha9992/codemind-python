n = int(input())
t = n
max1 = 0
while t!=0:
    r = t%10
    if r > max1:
        max1 = r
    t = t//10
print(max1)