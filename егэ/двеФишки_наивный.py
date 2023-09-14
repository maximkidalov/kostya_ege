n = int(input())
arr = list(map(int, input().split()))
sum = int(input())


def twosum(numbers, X):
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == X:
                return numbers[i], numbers[j]
    return None, None


res = ()
res = twosum(arr, sum)
if res == (None, None):
    print(None, end=' ')
else:
    for i in range(len(res)):
        print(res[i], end=' ')