n = eval(input())

def las():
    k = [1]
    yield 1
    while True:
        m = []
        l = k[0]
        count = 1
        for i in k[1:]:
            if l == i:
               count += 1
            else:
                m.append(count)
                yield count
                m.append(l)
                yield l
                l = i
                count = 1
        m.append(count)
        yield count
        m.append(l)
        yield l
        k = m       

k = 0
for i in las():
    if k == n:
        print(i)
        print()
        break
    else:
        k+=1
