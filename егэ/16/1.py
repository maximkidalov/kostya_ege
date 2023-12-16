def F(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return F(n-1) * F(n-2) + 1


print(F(6))
