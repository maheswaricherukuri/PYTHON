t = int(input()) #No.of Test Cases
for i in range(t):
    x,y,a,b=map(int,input().split())
    #print(x,y,a,b)         # Writing output to STDOUT
    if (x*y)==(a+b):
        print("Yes")
    else:
        print("No")
