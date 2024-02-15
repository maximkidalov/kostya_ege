f = open('26/58493.txt')
n = int(f.readline())  # кол-во авто

a = []  # массив для хранения всего
for i in range(n): # закидываем все данные в массив а
    start, time, type = f.readline().split()
    start = int(start)
    time = int(time)
    a.append([start, start + time, type])
a.sort()

l_a = [-1] * 80 # места для легковыйх
m_a = [-1] * 20 # места для всех
cnt_l = 0 # счетчик припаркванных легковых за все время
cnt_e = 0 # счетчик всех уехавших (потому что все занято)

for x in a:
    start, end, type = x
    parking = False
    if type == 'A': # если легковая
        for i in range(80): # если есть места для легковых
            if l_a[i] <= start:
                l_a[i] = end
                parking = True
                cnt_l += 1
                break
        if parking == False: # если нет мест для легковых
            for i in range(20):
                if m_a[i] <= start:
                    m_a[i] = end
                    parking = True
                    cnt_l += 1
                    break
    if type == 'B': # если автобус
        for i in range(20):
            if m_a[i] <= start:
                m_a[i] = end
                parking = True
                break
    if parking == False: # если нет места
        cnt_e += 1

print(cnt_l, cnt_e)