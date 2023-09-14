p = open("36037.txt").readline()
q = p.replace("XZZY", "Q")
o = 0
n = 0
for i in range(len(q)):
    if q[i] == "Q":
        n = max(o + 3, n)
        o = 3
    else:
        o += 1
n = max(o, n)
print(n)