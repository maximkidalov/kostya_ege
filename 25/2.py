for x in range(244143, 1367822):
    divs = set()
    for d in range(1, round(x ** 0.5) + 1):
        if x % d == 0:
            divs.add(d)
            divs.add(x // d)
            if len(divs) > 5:
                break
    if len(divs) == 5:
        print(sorted(divs)[2:-1])
