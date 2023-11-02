D = list(range(17, 59))
C = list(range(29, 81))
A = []
for x in range(1, 1000):
    if ((x in D) <= (((not (x in C)) and (not (x in A))) <= (not (x in D)))) is False:
        A.append(x)
print(A)

# [17,29]
# 29-17 = 12
