s = input()
flag = True
for i in s:
    if s.count(i) != 1:
        flag = False
        break
print(flag)