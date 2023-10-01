n = int(input())
arr = list(map(int, input().split()))
s = [str(i) for i in arr]
res = int("".join(s))
res += 1
pr = list(map(int, str(res)))
for i in pr:
    print(i, end = ' ')