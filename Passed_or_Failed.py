a = list(map(int,input().split()))
flag = 0
for i in range(0,5):
    if (a[i]>=35):
        flag+=1
if(flag < 5):
    print("FAILED")
else:
    print("PASSED")