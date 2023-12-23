cnt = 0
n = 452022
while cnt != 5:
    deliteli = []
    for i in range(2, n):
        if n % i == 0:
            deliteli.append(i)
    if len(deliteli) != 0:
        M = min(deliteli) + max(deliteli)
        if M % 7 == 3:
            print(n, M)
            cnt += 1
    n += 1
