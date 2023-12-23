def prost(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


maximum = 0
for i in range(631632, 684934):
    for d in range(2, round(i ** 0.5) + 1):
        if d * (i // d) == i and prost(d) and prost(i // d) and d != i // d:
            if i // d - d > maximum:
                maximum = i // d - d
        break
print(d, i // d)
