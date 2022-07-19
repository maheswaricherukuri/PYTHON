s=input()
l=len(s)
j=0
for i in s:
    j+=1
    if i==s[-j]:
        f=1
    else:
        f=0
        break
if f==0:
    print("NO")
else:
    print("YES")
