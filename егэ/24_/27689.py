f = open('27689_джекпот.txt').readline()
k = m = 0
for i in range(len(f)):
    if (f[i] == 'X' and k%3 == 0) or (f[i] == 'Y' and k%3 == 1) or (f[i] == 'Z' and k%3 == 2):
        k += 1
        m = max(m, k)
    elif f[i] == 'X': k = 1
    else: k = 0
print(m)