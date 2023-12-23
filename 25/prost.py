def prost(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


print(prost(25))
