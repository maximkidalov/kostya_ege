def prost(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


count = 0
for i in range(7178551, 7178660):
    if prost(i):
        count += 1
        print(count, i)
