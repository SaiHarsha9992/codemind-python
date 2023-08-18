a,b,c,d,e = map(int,input().split())
avg = (a+b+c+d+e)//5
if(avg >= 90):
    print("Grade A")
elif(avg >= 80):
    print("Grade B")
elif(avg >= 70):
    print("Grade C")
elif(avg >= 60):
    print("Grade D")    
elif(avg >= 40):
    print("Grade E")    
else:
    print("Grade F")