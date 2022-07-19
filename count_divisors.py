i,k,r=map(int,input().split())
print(len([j for j in range(i,k+1) if j%r==0]))
