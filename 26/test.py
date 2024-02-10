f = open('26/test.txt')

cubes = sorted([int(i) for i in f], reverse=True)

print(cubes)
