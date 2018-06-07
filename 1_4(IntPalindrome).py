num = eval(input())
m = 0
n = num
while (n != 0):
    m = m * 10 + int(n % 10)
    n = int(n / 10)

if m == num:
    print ('YES\n')
else:
    print ('NO\n')
