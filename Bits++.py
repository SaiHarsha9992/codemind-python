t = int(input())
arr = []
for i in range(t):
    arr.append(input())
c = 0
for i in arr:
    if i[-1] == '+'or i[0] == '+':
        c += 1
    elif i[-1] == '-' or i[0] == '-':
        c -=1
print(c)
    