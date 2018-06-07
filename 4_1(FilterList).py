k = eval(input())
m, n = eval(input())
kn = []
for i in range(len(k)):
    if (i%m != 0) and (k[i]%n != 0):
        kn.append(k[i])
print(kn)
print()
