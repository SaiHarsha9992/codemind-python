ch = input()
a = 'QWERTYUIOPASDFGJHKLZXCVBNM'
B = 'qwertyuiopasdfghjklzxcvbnm'
if (ch in a):
    print("uppercase alphabet")
elif(ch in B):
    print("lowercase alphabet")
else:
    print("not an alphabet")