p = input().lower().split()
dict = {}
while len(p)==2:
    if p[0] in dict:
        dict[p[0]].add(p[1])
    else:
        dict[p[0]] = set([p[1]])
    if p[1] in dict:
        dict[p[1]].add(p[0])
    else:
        dict[p[1]] = set([p[0]])
    p = input().lower().split()
inp = p[0]
outp = input().lower()
s = set()
s.add(inp)
s1 = set()
while (s1 != s) and (outp not in s):
    s2 = s1
    s1 = s
    for i in (s1-s2):
        s = s|dict[i]
        if outp in s:
            break
if outp in s:
    print('YES\n')
else:
    print('NO\n')
