n = int(input())
flag = False
for i in range(1,(n//2)+1):
    if i * i == n:
        flag = True
if flag == True:
    print("True")
else:
    print("False")