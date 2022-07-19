#problem 9 : minimize cost
'''
n,k=map(int,input().split())
a=list(map(int,input().split()))
t=[0]*n
min_cost=0
#print(n,k,a,t)
for i in range(n-1):
    t1=a[i]
    #print(t1)
    if t1>0:
        j = i  # position for t array
######### approach 1:  less than a[i] until K
        cnt=1 # to split the value of a[i]        
        while j>k:
            if t1>=cnt:
                t[i]-=cnt
                t[j+1]=cnt
                t1 -= cnt
                cnt+=1
                j+=1
######### approach 2 :
       while k>0:
            #print(t1,k)
            if t1>k and j<k:
                t[i]-=k
                t[j+1]=k
                t1 -= k
                k-=1
             #   print(t)
            else:
                t[i] -= t1
                t[j + 1] = t1
              #  print(t)
                break
    i+=1
#print(a,t)
i=0
while n>i:
 #   print(abs(a[i]+t[i]))
    min_cost += abs(a[i]+t[i])
    i+=1

print(min_cost)
#print(a,t)
'''
