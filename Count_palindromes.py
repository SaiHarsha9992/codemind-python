def isPali(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False
n = int(input())
arr = list(map(int, input().split()))
c = 0
for i in arr:
    if isPali(i):
        c += 1
print(c)