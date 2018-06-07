s = eval(input())
n = int(len(s)/2) - 1 + (len(s)%2)
print (s[n*2::-2] + s[1::2])

