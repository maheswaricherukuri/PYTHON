t=int(input()) # no.of test cases
s=[6,2,5,5,4,5,6,3,7,6]
j,no_matches=0,0
while t>0:
    n = input()  # number that tells u the no.of match sticks u get
    no_matches=sum(s[int(j)] for j in n)
    if (no_matches % 2) == 0:
        print("1" * (no_matches//2))
    else:
        print("7",end='')  # 7 is the largest number with least sticks 3
        print("1" * ((no_matches//2) -1))
    t-=1
