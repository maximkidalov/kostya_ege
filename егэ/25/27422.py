for i in range(174457, 174506):
    divs = set()
    for l in range(1, round(i ** 0.5)+1):
        if i % l == 0:
            divs.add(l)
            divs.add(i//l)
            if len(divs) > 4:
                break
    if len(divs) == 4:
        print(sorted(divs))