n = int(input('n:'))
m = int(input('m:'))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
s = []
for i in range(len(a)):
    s.append(sum(a[i]))
print(a[s.index(max(s))], 'largest sum:', max(s), a[s.index(min(s))], 'smallest sum:', min(s))
