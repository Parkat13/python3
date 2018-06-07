s = eval(input())
m1, m2 = s[0],s[0]
for i in s:
    if i>m1:
        if m1>m2:
            m2 = m1
        m1 = i
    elif (i>m2)and(i!=m1):
        m2 = i
    elif (m1 == m2):
        m2 = i
if m1 == m2:
    print('NO\n')
else:
    print(m2)
    print('\n')
