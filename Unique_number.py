n = input()
s = ''.join(sorted(n))
flag = True
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        flag = False
        break
if flag == True:
    print("Unique Number")
else:
    print("Not Unique Number")