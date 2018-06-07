p = eval(input())
l = eval(input())

def nInPos():
    global p
    num = 0
    while num!=len(p):
        j = p[num]
        num += 1
        v = []
        a = j[0]
        while len(v)==0 or not(a==v[-1]):
            yield a
            v.append(a)
            if a%j[1]==0:
                a = a/j[1] + j[2]
            else:
                a = a + j[3]

k = 0
for i in nInPos():
    if k == l:
        print(int(i))
        print()
        break
    else:
        k+=1
else:
 print('NO\n')
