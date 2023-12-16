# умный способ
x = 36
divs = []
for d in range(1, round(x ** 0.5) + 1):
    if x % d == 0:
        divs.append(d)
        divs.append(x // d)
print(divs)