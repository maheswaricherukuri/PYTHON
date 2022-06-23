n=int(input())       # first input length of string
s=input()            # input string
consecutive_house=[] # empty array to add consecutive houses
out_arr=[""]*n       # output array when there are no consecutive houses
temp=0 # counter to find the consecutive houses
for i,j in enumerate(s): # (0,s[0])
    if j=="H":
        out_arr[i]=j
        temp+=1
        if i==n-1:
            consecutive_house.append(temp) #consecutive_house[] will be having value of 1 only or empty
    else:
        out_arr[i]="B"
        if temp>0:
            consecutive_house.append(temp)
            temp=0
if len(consecutive_house)==0 or max(consecutive_house)==1:
    print("YES")
    print(''.join(out_arr))
else:
    print("NO")
