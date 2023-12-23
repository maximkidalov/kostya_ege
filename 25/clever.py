# умный способ
x = 36
divs = set()  # set
for d in range(1, round(x ** 0.5) + 1):
    if x % d == 0:
        divs.add(d)
        divs.add(x // d)
print(sorted(divs))  # опять list
