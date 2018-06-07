n = eval(input())
k = 0
for i in dir(n):
    if type(eval('n.'+i)) == type(k):
        k += 1
print(k)
print()
