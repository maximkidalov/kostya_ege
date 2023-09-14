# поиск делителей глупым способом
x = 36
divs = []  # список
for d in range(1, x + 1):
    if x % d == 0:
        divs.append(d)
print(divs)
