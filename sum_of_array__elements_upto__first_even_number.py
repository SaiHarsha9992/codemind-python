n = int(input())
arr = list(map(int, input().split()))
s = 0
for i in arr:
    if i%2 == 1:
        s += i
    else:
        break
print(s)