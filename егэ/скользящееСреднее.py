n = int(input())
arr = list(map(int, input().split()))
k = int(input())


def moving_average(timeseries, K):
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(timeseries[0:K])
    result.append(current_sum / K)
    for i in range(0, len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result


arr = moving_average(arr, k)
for i in range(len(arr)):
    print(arr[i], end=' ')