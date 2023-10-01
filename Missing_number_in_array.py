t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = 0
    s1 = 0
    for j in range(1,n+1):
        s += j
    for k in arr:
        s1 += k
    print(s-s1)