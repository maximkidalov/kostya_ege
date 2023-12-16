def F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + 2 + F(n-1)
    else:
        return 2 * F(n-2)


print(F(24))
