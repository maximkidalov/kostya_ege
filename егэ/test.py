n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = []

for i in range(n):
    arr3.append(arr1[i])
    arr3.append(arr2[i])

for i in range(len(arr3)):
    print(arr3[i], end=' ')