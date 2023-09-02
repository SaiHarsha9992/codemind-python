n = int(input())
x = 0
for i in range(1,n+1):
    if i * (i+1) == n:
        x = 1
        break
if x == 1:
    print("YES")
else:
    print("NO")