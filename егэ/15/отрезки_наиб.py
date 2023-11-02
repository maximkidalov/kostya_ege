P = list(range(3, 14))
Q = list(range(12, 23))
A = list(range(1, 100))
for x in range(1, 100):
    if (((x in A) <= (x in P)) or (x in Q)) is False:
        A.remove(x)
print(A)

# 3-есть
# 22-есть
# 22-3=19