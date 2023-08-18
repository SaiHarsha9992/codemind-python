n = int(input())
c = 0.00
if(n<=199):
    c = 1.20
elif(n>=200 and n < 400):
    c = 1.50
elif(n >= 400 and n < 600 ):
    c = 1.80
elif(n>=600):
    c = 2.00
b = n * c
ts = 0
if(b>=400):
    ts = b+(b*0.15) 
elif(b<400):
    ts = b+100
    
print(f"{ts:.2f}")   