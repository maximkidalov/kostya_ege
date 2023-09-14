def counting_sort(arr):
    # Находим максимальное и минимальное значения в массиве
    min_val = min(arr)
    max_val = max(arr)

    # Создаем массив для подсчета частоты значений
    count_arr = [0] * (max_val - min_val + 1)

    # Подсчитываем частоту каждого значения
    for num in arr:
        count_arr[num - min_val] += 1

    # Восстанавливаем отсортированный массив
    sorted_arr = []
    for i, count in enumerate(count_arr):
        sorted_arr += [i + min_val] * count

    return sorted_arr


arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)
