n = int(input())
arr = list(map(int, input().split()))
m1 = -1
m2 = -1
m3 = -1
for i in arr:
    if(i>m1):
        m1=i
for i in arr:
    if(i>m2 and i!=m1):
        m2=i
for i in arr:
    if(i>m3 and i!=m2 and i!=m1):
        m3=i
        
if(m3==-1):
    print(m1)
else:
    print(m3)