n = int(input())
m = int(input())
a = [list(map(int, input().split()))[:m:] for i in range(n)]
s = 0
for i in a:
    for j in i:
        s += j
print(s)