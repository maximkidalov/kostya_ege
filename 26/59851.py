f = open("26/59851.txt")
s = list(map(int, f.readlines()))
s = s[1:]
s.sort(reverse=True)
print(sum(s[len(s)//3:]), sum(s)-sum(s[2::3]))