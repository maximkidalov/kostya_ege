# Поиск количества программ по заданному числу
def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x + 2, y) + f(x * 5, y)


print(f(2, 50))
