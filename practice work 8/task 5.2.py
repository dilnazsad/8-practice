def smallestInRow(mat):
    minm = min(mat)
    return minm


n = int(input('n:'))
m = int(input('m:'))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
minm = []
for i in range(n):
    minm.append(smallestInRow(a[i]))
print(minm)

for i in range(len(minm)):
    if minm[i] % 2 == 0:
        minm[i] = 0
    else:
        minm[i] = 1
print(minm)
