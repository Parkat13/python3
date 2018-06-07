s = set(eval(input()))
x = max(s)
th = set()
l = [i**2 for i in range(1,x)]
for i in l:
    for j in l:
        if ((i+j+1)>x) or (j>i):
           break
        for k in l:
            m = i + j + k
            if (m > x) or (k>j):
                break
            th.add(m)
print(len(s&th))
print()
