n, m = map(int ,input().split())
a = [sum(list(map(int, input().split()))[:m:]) for i in range(n)]
m = 0
for i in a:
    if i > m:
        m = i
print(m)