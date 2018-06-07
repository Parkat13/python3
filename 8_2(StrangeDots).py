class Dots:
    def __init__(self, x, y):
        self.left, self.right = x, y
    def __getitem__(self, item):
        s = str(item)[6:-1].split()
        if type(item) == int:
            n = (self.right - self.left)/(float(item) - 1)
            r = []
            x = float(self.left)
            for i in range(item):
                r.append(x)
                x += n
            return  (r)
        elif s[2] == 'None':
            n = (self.right - self.left)/(float(s[1][0:-1]) - 1)
            r = []
            x = float(self.left)
            return  (self.left + n*int(s[0][0:-1]))
        else:
            n = (self.right - self.left)/(float(s[2]) - 1)
            r = []
            s1, s2 = 0, 0
            if s[0][0:-1] == 'None':
                s1 = None
                s10 = 0
            else:
                s1 = int(s[0][0:-1])
                s10 = s1
            if s[1][0:-1] == 'None':
                s2 = None
                s20 = int((self.right-self.left)/n) + 1
            else:
                s2 = int(s[1][0:-1])
                s20 = s2
            for i in range(s10,s20):
                r.append(self.left + i*n)
            return  (r)


