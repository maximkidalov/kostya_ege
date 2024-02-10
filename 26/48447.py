f = open('26/48447.txt')
n = f.readline()
# читает первую строку
cubes = sorted([int(i) for i in f], reverse=True)
# читает оставшиеся строки файла, преобразует их в целые числа, сортирует их по убыванию и сохраняет в списке cubes
cklad = []
while len(cubes) > 0:  # повторяется, пока в списке cubes есть кубы
    block = [cubes.pop(0)]  # берет первый куб из cubes и начинает новый блок
    for i in range(len(cubes)):  # перебирает оставшиеся кубы
        if (block[-1]-cubes[i]) >= 5:
# проверяет, является ли разница между последним кубом в текущем блоке и текущим кубом больше или равна 5.
            block.append(cubes[i]) # Если да, то добавляет текущий куб в блок
            cubes[i] = ''  # помечает добавленный куб в списке cubes как пустой
    cubes = [x for x in cubes if x != '']  #  удаляет пустые строки (помеченные как обработанные) из списка cubes
    cklad.append(block)  # добавляет готовый блок в список cklad
print(len(cklad), max(len(c) for c in cklad))
# выводит количество сформированных блоков (len(cklad)) и максимальную длину любого блока (max(len(c) for c in cklad)).
