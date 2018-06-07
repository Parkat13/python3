s = input()
n = 0
fl = True
while s!='':
    c = s.split()
    for i in c:
        if i.isdigit() or (i[0]=='-' and i[1:].isdigit()):
            if fl:
                fl = False
                n = int(i)
            elif n < int(i):
                n = int(i)
    s = input()
print(n)
print()
