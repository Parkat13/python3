m,n = eval(input())
mat = []
for i in range(n):
    v  = []
    for j in range(m):
        v.append(-1)
    mat.append(v)
nap = [[0,1],[1,0],[0,-1],[-1,0]]
s = 0
x,y = 0,0
for i in range(n*m):
    if x==n or y ==m or x==-1 or y==-1 or mat[x][y]!=-1:
        x -= nap[s][0]
        y -= nap[s][1]
        s = (s+1)%4
        x += nap[s][0]
        y += nap[s][1]
    mat[x][y] = i%10
    x += nap[s][0]
    y += nap[s][1]
for i in range(n):
    s = ''
    for j in range(m):
        s = s + str(mat[i][j]) + ' '
    print(s)
print()
