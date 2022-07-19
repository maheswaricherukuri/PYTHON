str1=input().upper()
z=int(str1.count("Z"))
#print(z)
o=int(str1.count("O"))
#print(o)
if o/z==2:
    print("Yes")
else:
    print("No")
