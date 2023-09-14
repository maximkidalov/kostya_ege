# Операции в одной СС
for x in '0123456789ABCDE':
    x1 = '123' + str(x) + '5'
    x2 = '1' + str(x) + '233'
    res = int(x1, 15) + int(x2, 15)
    if res % 14 == 0:
        res = res // 14
        print(res)
        break