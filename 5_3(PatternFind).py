s = input()
c = input()
k = 0
for i in range(len(s)):
    if (s[i] == c[k]) or (c[k] == '@'):
        k += 1
        if k == len(c):
            print(i-k+1)
            print()
            break
    else:
        k = 0
else:
    print('-1')
    print()
