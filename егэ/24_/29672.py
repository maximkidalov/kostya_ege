f = open('24_/29762.txt')
a = 0
for string in f:
    if (string.count('A') < string.count('E')):
        a += 1
print(a)
