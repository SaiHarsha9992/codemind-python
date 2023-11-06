s = input()
present = '1234567890'
total = 0
for i in s:
    if i in present:
        total += int(i)
print(total)