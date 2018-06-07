import math
import decimal
a = decimal.Decimal(eval(input()))
i = decimal.Decimal(0.0)
m = decimal.Decimal(0.0)
def pigen(m):
    m += decimal.Decimal((-1)**i)*(decimal.Decimal(4.0)/decimal.Decimal(i * decimal.Decimal(2.0) + decimal.Decimal(1.0)))
    return m
pi1 = decimal.Decimal(pigen(m))
i += decimal.Decimal(1.0)
m = pi1
pi2 = pigen(m)
i += decimal.Decimal(1.0)
m = pi2
while math.fabs(pi1-pi2) > a:
    pi1 = pi2
    pi2 = pigen(m)
    m = pi2
    i += decimal.Decimal(1.0)
print(i-1)
