def find_lcs(s1, s2):
    m = len(s1)  # Длина первой строки
    n = len(s2)  # Длина второй строки
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # Создание матрицы dp для хранения результатов

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:  # Если символы равны, увеличиваем длину LCS
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Иначе, берем максимум из предыдущих результатов
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp[m][n])wed

    lcs_length = dp[m][n]  # Длина наибольшей общей подпоследовательности
    lcs = [''] * lcs_length  # Создание списка для хранения символов LCS
    i = m  # Индекс для строки s1
    j = n  # Индекс для строки s2

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:  # Если символы равны, добавляем символ к LCS
            lcs[lcs_length - 1] = s1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Иначе, двигаемся в направлении с максимальным значением
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)  # Возвращаем наибольшую общую подпоследовательность в виде строки


# Пример использования
s1 = "AGGTAB"
s2 = "GXTXAYB"
lcs = find_lcs(s1, s2)  # Находим саму наибольшую общую подпоследовательность
print("LCS:", lcs)  # Выводим наибольшую общую подпоследовательность
