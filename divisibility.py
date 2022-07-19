n=int(input())
a=list(map(int,  input().split()))
num,i=0,0
x=""
while i<n:
    x+=str(a[i])[-1]
    i+=1
if int(x)%10==0:
    print("Yes")
else:
    print("No")
