f = open("26/59852.txt")
s = list(map(int, f.readlines()))
n = s[0]  # количество деталей
k = s[1]  # количество контейнеров
d = s[2:n+2]  # детали
p = s[n+2:]  # контейнеры
count = 0
maxv = 0
for i in range(n):
    for j in range(k):
        if d[i] <= p[j]:
            count += 1
            p[j] -= d[i]
            if d[i] > maxv:
                maxv = d[i]
            break
print(count, maxv)
