n = int(input())
arr = list(map(int, input().split()))
e = 0
o = 0
for i in range(n):
    if i%2 == 0:
        e += arr[i]
    else:
        o += arr[i]
print(abs(e-o))

