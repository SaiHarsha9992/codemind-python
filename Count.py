n = int(input())
arr = list(map(int, input().split()))
o = 0 
e = 0
for i in arr:
    if i%2 == 0:
        e += 1
    elif i%2 == 1:
        o += 1
print(e,o)