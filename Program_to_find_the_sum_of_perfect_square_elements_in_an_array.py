import math
def is_perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n
n = int(input())
arr = list(map(int, input().split()))
s = 0
for i in arr:
    if is_perfect_square(i):
        s += i
print(s)