n = eval(input())
i = 2
m = 0
fl = 0
while i < n:
    m = i
    while m < n:
        m *= i
        if n == m:
            print ('YES\n')
            fl = 1
            break
    i += 1
    if fl == 1:
       break
else:
    print ('NO\n')

