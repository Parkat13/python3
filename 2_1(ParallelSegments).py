import decimal
x1,y1,x2,y2,x3,y3,x4,y4 = eval(input())

if ((decimal.Decimal(y2)-decimal.Decimal(y1))/(decimal.Decimal(x2)-decimal.Decimal(x1))) == ((decimal.Decimal(y4)-decimal.Decimal(y3))/(decimal.Decimal(x4)-decimal.Decimal(x3))):
    print('YES\n')
elif (x1 == x2) and (x3 == x4):
    print('YES\n')
else:
    print('NO\n')
