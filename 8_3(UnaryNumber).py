class Unary:
    def __init__(self, s):
        self.strp = s
        self.n = len(s)
    def __str__(self):
        return(self.strp)
    def __invert__(self):
        self.n = int(self.n/2)
        s = ''
        for i in range(self.n):
            s = s + '|'
        self.strp = s
        return (self)
    def __ior__(self, k):
        self.strp = self.strp + k.strp
        self.n = len(self.strp)
        return(self)
    def __pos__(self):
        self.n += 1
        self.strp = self.strp + '|'
        return(self)
    def __iter__(self):
        return(iter(list(Unary(self.strp[i]) for i in range(self.n))))
    def __bool__(self):
        if len(self.strp) == 0:
            return False
        else:
            return True
    def __len__(self):
        return(self.n)

