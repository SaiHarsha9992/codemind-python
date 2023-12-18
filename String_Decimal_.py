t = int(input())
for i in range(t):
    s = input()
    n = "1234567890"
    c = 0
    for k in range(len(s)):
        if s[k] in n:
            c += 1
    print("True" if c == len(s) else "False")