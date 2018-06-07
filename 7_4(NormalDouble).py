class Normal:
    def __init__(self, start):
        self.n = start
    def swap(self, other):
        self.n, other.n = other.n, self.n
    def what(self):
        return self.n

class Double:
    def __init__(self, start):
        self.n = start*2
    def swap(self, other):
        self.n, other.n = other.n*2, self.n*2
    def what(self):
        return self.n*2
