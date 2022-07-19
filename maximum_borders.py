t = int(input())
while (t>0):
    n, m = input().split()
    n=int(n)
    m=int(m)
    x, y, y_max= 0,0,0
    for i in range(n):
        y=str(input()).count('#')  # column count
        if y>y_max:
            y_max=y
    print(y_max)
    t-=1
