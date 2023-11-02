for A in range(1, 1000):
    A_podoshel = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((2*x + y != 70) or (x < y) or (A < x)) is False:
                A_podoshel = False
                break
        if A_podoshel is False:
            break
    if A_podoshel is True:
        print(A)
