n, m = map(int,input().split())
arr = [sum(list(map(int, input().split()))[:m:]) for i in range(n)]
print(sum(arr))