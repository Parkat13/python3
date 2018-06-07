s = eval(input())
m = 0
m1 = s[0]
m2 = s[1]
for i in range(len(s)-2):
    m = min(m1,m2) + s[i+2]
    m1, m2 = m2, m
print(m)
print('\n')
