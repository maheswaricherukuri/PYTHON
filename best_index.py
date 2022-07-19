N = int(input())
f = []
while N > 0:
    x = 0
    l = []
    while sum(l) < N:
        x = x + 1
        l.append(x)
    if sum(l) > N:
        l.pop()
    f.append(sum(l))
    N -= 1
A = input().split(" ")
C = [int(x) for x in A]
l = []
for i, j in zip(range(len(C)), f):
   # print(i,j)
    l.append(sum(C[i:i + j]))
print(max(l))
