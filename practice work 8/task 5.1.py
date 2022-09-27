def printArray(arr, m, n):
    for i in range(m):
        for j in range(n):
            print(arr[i][j], end=' ')
        print()


def sortArr(arr, m, n):
    for i in range(m):
        arr[i].sort()
    print()


n = int(input('n:'))
m = int(input('m:'))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
printArray(a, m, n)

sortArr(a, m, n)
print('sorted matrix:')
printArray(a, m, n)
