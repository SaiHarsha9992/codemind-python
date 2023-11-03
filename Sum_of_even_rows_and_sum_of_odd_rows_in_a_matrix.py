n, m = map(int, input().split())
arr = [list(map(int, input().split()))[:m:] for i in range(n)]
e = 0
o = 0
for i in arr:
    if arr.index(i)%2 == 0:
        e += sum(i)
    else:
        o+= sum(i)
print(e,o)