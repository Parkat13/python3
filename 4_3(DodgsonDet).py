import decimal
decimal.getcontext().prec = 35
mat = []
mat.append(eval(input()))
n = len(mat[0])
d = decimal.Decimal(1)
dn  = decimal.Decimal(1.0)
for i in range(1,n):
    mat.append(eval(input()))
while len(mat) > 1:
    b = []
    if mat[0][0]==decimal.Decimal(0):
        k = 0
        for i in range(len(mat)):
            if mat[i][0]!= decimal.Decimal(0):
                k = i
                break
        c = []
        for i in range(len(mat)):
            if i == 0:
                c.append(mat[k])
            elif i == k:
                c.append(mat[0])
            else:
                c.append(mat[i])
        mat = c
        d *= decimal.Decimal((-1)**(2*k - 1))
    #d *= decimal.Decimal(mat[0][0]**(len(mat)-2))
    for i in range(len(mat)-1):
        v = []
        for j in range(len(mat)-1):
            v.append((decimal.Decimal(mat[0][0])*decimal.Decimal(mat[i+1][j+1])-decimal.Decimal(mat[i+1][0])*decimal.Decimal(mat[0][j+1]))/dn)
        b.append(v)
    dn = decimal.Decimal(mat[0][0])
    mat = b
#if len(mat) == 2:
#    s = decimal.Decimal(mat[0][0])*decimal.Decimal(mat[1][1])-decimal.Decimal(mat[0][1])*decimal.Decimal(mat[1][0])
#else:
s = decimal.Decimal(mat[0][0])
print(round(s/d))
print()
