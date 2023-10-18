n = int(input())
arr = list(map(int, input().split()))
flag = False
for i in range(n):
    if arr[i]%2 != 0:
        if i%2 != 0:
            flag = True
        else:
            flag = False
            break
print(flag == True)