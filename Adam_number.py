def Rev(n):
    s = str(n)
    return int(s[::-1])
n = int(input())
sq1 = n**2
n1 = Rev(n)
sq2 = n1**2
print(sq1 == Rev(sq2))