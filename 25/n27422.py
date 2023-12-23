for i in range(174457, 174506):
    deliteli = []
    for j in range(2, i):
        if i % j == 0:
            deliteli.append(j)
    if len(deliteli) == 2:
        print(deliteli)
