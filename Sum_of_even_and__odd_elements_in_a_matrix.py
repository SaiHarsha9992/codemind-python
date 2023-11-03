n, m = map(int, input().split())
arr = [list(map(int,input().split()))[:m:] for i in range(n)]
e = 0
o = 0
for i in arr:
    for j in i:
        if j%2 == 0:
            e += j
        else:
            o += j
print(e,o)