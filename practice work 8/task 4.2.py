n = int(input('n:'))
m = int(input('m:'))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()

a = [[1 if x > 0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x <= i else '' for x in range(len(a[i]))], '')
