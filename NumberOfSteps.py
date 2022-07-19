n=int(input())
a1=list(map(int,(input().split())))
b1=list(map(int,(input().split())))
c=int(min(a1))
ans=0
for i in range(n):
    a,b,x=a1[i],b1[i],0
    #print("i:%s a1[i]:%s b1[i]:%s c:%s ans:%s" %(i,a1[i],b1[i],c,ans))
    if a==c:
        ans += 0
        # ans1 += 1
        #print("ans :", ans)
    elif a >c and a>=b and ans>-1:
        x=((a-c)/b)
        #print("while Ans:" ,ans1)
        #print("x= ((%s - %s)/%s" % (a,c,b), x)
        if (x-int(x))==0:
            ans+=x
            #print("ans+=x is :" , ans)
        else:
            ans=-1
            #print(" (x-int(x))==0 is :", ans)
    else:
        ans=-1
        #print("a != c and a>b and ans>-1 : ", ans)
print(int(ans))
