bs = int(input())
da = 0.00
hra = 0.00
if(bs <= 10000):
    da = 0.8
    hra = 0.2
elif (bs <= 20000):
    da = 0.9
    hra = 0.25
elif(bs > 20000):
    da = 0.95
    hra = 0.3
p = bs+(da*bs)+(hra*bs)
print(f"{p:.2f}")