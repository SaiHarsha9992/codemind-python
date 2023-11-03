n, m = map(int, input().split())
a = [list(map(int, input().split()))[:m:] for i in range(n)]
for i in a:
    print(sum(i), end = ' ')