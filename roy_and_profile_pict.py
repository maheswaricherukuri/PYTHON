l=int(input())
n=int(input())
for i in range(0,n):
    w,h=map(int,input().split())
    if (w==l and h==l) or (w>l and w==h):
        print("ACCEPTED")
    elif h<l or w<l:
        print("UPLOAD ANOTHER")
    else:
        print("CROP IT")
