def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Подсчитываем количество элементов с определенными цифрами
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Вычисляем позиции элементов в итоговом массиве
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Размещаем элементы в правильной позиции в итоговом массиве
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Копируем отсортированный массив в исходный массив
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    max_value = max(arr)

    # Применяем сортировку подсчетом для каждого разряда
    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

    return arr


arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print(sorted_arr)
