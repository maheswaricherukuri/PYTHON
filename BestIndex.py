n=int(input()) # no.of elements
a=list(map(int,input().split()))   # array of 'n' elements
n1=[]
index_prev=0
n1 += (((i * (i + 1)) // 2) for i in range(n) if ((i * (i + 1)) // 2)<=n)
for j in range(n):
    max_ele = max(i for i in n1 if i <= n) # maximum element to be considered for sum
    #print(j,max_ele,max_ele+j)
    index = max(sum(a[k] for k in range(j, max_ele+j)),index_prev)
    index_prev = index
    n-=1
print(index)
