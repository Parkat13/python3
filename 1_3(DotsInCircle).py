x0, y0, r = eval(input())
fl = 0
x1, y1 = eval(input())
while (x1 != 0) and (y1 != 0):
    if ((x1 - x0)**2 + (y1 - y0)**2) > r**2:
        fl = 1
    x1, y1 = eval(input())
if fl:
    print ('NO\n')
else:
    print ('YES\n')


