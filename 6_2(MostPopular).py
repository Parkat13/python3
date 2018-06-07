s = input().lower().split()
dict = {}
m = 0
for i in s:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
    if dict[i]>m:
        m = dict[i]
n = 0
for i in dict:
    if dict[i] == m:
        n += 1
print(n)
print()


