with open('46982.txt') as f:
    s = f.readline()
    s = s.split('E')
    k = 0
    for i in range(len(s)):
        if (len(s[i]) >= 10) and ('F' not in s[i]):
            k += 1
print(k)