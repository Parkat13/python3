class A:
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return('/' + str(self.n) + '/')
    def __add__(self, other):
        if type(self)==type(A(8)):
            return(A(self.n + other.n))
        elif type(self)==type(B(8)) and type(other)==type(A(8)):
            return(A(self.n + other.n))  
        else:
            return(B(self.n+other.n))
    def __iter__(self):
        return(iter(self.n))
    def __radd__(self, other):
        if type(self)==type(A(8)):
            return(A(self.n + other.n))
        else: 
            return(C(self.n + other.n)) 


class B:
    def __init__(self, n):
        self.n = n
    def __str__(self):
        return('|' + str(self.n) + '|')
    def __mul__(self, other):
        return(B(self.n*other.n))
    def __rmul__(self, other):
        return(B(self.n*other.n))

class C(B,A):
    def __init__(self, n):
        self.n = n



