import math
p = int(input())
r = int(input())
t = int(input())
c = p*math.pow(1+((r/100)),t)-p
print(f"{c:.2f}")