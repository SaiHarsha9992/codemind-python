n = int(input())
arr = list(map(int, input().split()))
x = list(set(arr))
for i in x:
    print(i, end = ' ')