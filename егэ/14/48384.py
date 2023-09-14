# Операции в разных СС с двумя переменными
result_search = []
for x in '012345678':
    for y in '012345678':
        t = int('88' + x + '4' + y, 9) + int('7' + x + '44' + y, 11)
        if t % 61 == 0:
            result_search.append(t)
if result_search:         
    print(min(result_search) // 61)