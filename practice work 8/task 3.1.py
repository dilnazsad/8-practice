n = int(input('n:'))
m = int(input('m:'))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
b = "YES"
for i in range(m):
    for j in range(n):
        if a[i][j] != a[j][i]:
            b = "NO"
            break
print(b)