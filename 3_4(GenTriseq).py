def fun():
    for i in range(len(v)):
        for j in range(len(v)):
            if v[j]<=v[i]:
                yield v[j]

v = eval(input())
n = eval(input())
k = 0
for i in fun():
    if k == n:
        print(i)
        print()
        break
    else:
        k+=1
else:
 print('NO\n')

