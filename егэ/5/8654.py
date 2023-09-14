for i in range(1000, 10000):
    s = str(i)
    k1 = int(s[0]) * int(s[1])
    k2 = int(s[2]) * int(s[3])
    one = str(max(k1, k2))
    two = str(min(k1, k2))
    s1 = one + two
    if s1 == '124':
        print(i)
        break
