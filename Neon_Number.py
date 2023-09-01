n = int(input())
s = n**2
t = s
sum1 = 0
while t!=0:
    r = t%10
    sum1 += r
    t = t // 10
if sum1==n:
    print("Neon Number")
else:
    print("Not Neon Number")