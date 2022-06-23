t=int(input()) #no.of test cases
for l in range(t):
    g,p=map(int,input().split()) # cost of green and purple balloon
    n=int(input()) #no.of participants
    r=[input().split() for i in range(n)]  # result of each participant for q1 and q2
    a=sum(int(r[j][0]) for j in range(n))
    b=sum(int(r[k][1]) for k in range(n))
    res=min((a*g+b*p),(a*p+b*g))
    print(int(res))
