n = int(input())
arr = list(map(int,input().split()))
s = 0
for i in range(n):
    s+=arr[i]
print(s)