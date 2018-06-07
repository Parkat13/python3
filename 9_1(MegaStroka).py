class Stroka(str):
    def __init__(self,s):
        self.s = s
    def __neg__(self):
        self.s = self.s[::-1]
    def __mul__(self, other):
        s = ''
        if type(other) == int:
            for i in range(other):
                s = s + self.s
        else:
            for i in self.s:
                for j in other.s:
                    s = s + i + j
        return(Stroka(s))
    def __pow__(self, n):
        if n==0:
            return(Stroka(''))
        else:
            l = len(self.s)
            s = list(self.s[i] for i in range(l)) 
            for k in range(1, n):
                ind = 0
                for i in range((l**k)*(2**(k-1))):
                    a = s[ind]
                    s[ind+1:ind+1] = [self.s[0]] 
                    ind += 2
                    qq = ind
                    q = []
                    for j in self.s[1:]:
                        q.append(a)
                        q.append(j)
                        ind += 2
                    s[qq:qq] = q
            return(Stroka(''.join(s)))



