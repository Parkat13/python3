import math
p = input().lower().split()
dict = {}
s = set()
while len(p)==4:
    dict[(float(p[0]), float(p[1]), float(p[2]))] = p[3]
    s.add((float(p[0]), float(p[1]), float(p[2])))
    p = input().lower().split()
g = []
r = -1.0
for i in dict:
    s.remove(i)
    for j in s:
        m = math.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2 + (i[2] - j[2])**2)
        if m > r:
            r = m 
            g = [dict[i], dict[j]]
g.sort()
print(g[0] + ' ' + g[1] + '\n')
