# Посимвольное двоичное преобразование
def f(s):
    summa = 0
    for i in range(len(s)):
        summa += int(s[i])
    return summa


for n in range(1, 100):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    summa = f(s)
    s = s + str(summa % 2)
    summa = f(s)
    s = s + str(summa % 2)
    r = int(s, 2)  # перевод в десятичную систему
    if r > 43:
        print(r)
        break
