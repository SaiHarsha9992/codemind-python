s = input()
c = 0
for i in range(len(s)):
    if s[i] == '1' or s[i] == '2' or s[i] == '3' or s[i] == '4' or s[i] == '5' or s[i] == '6' or s[i] == '7' or s[i] == '8' or s[i] == '9' or s[i] == '0':
        c += 1
if c == 0:
    print(f"Doesn't contain digit")
else:
    print(f'Contains {c} digit')