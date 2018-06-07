import math
class Vector:
    def __init__ (self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def __add__ (self, other):
        return(Vector(self.x + other.x, self.y + other.y, self.z + other.z))
    def __sub__ (self, other):
        return(Vector(self.x - other.x, self.y - other.y, self.z - other.z))
    def __mul__ (self, num):
        return(Vector(self.x * num, self.y * num, self.z * num))
    def __truediv__ (self, num):
        return(Vector(self.x / num, self.y / num, self.z / num))
    def __matmul__ (self, other):
        return(self.x * other.x + self.y * other.y + self.z * other.z)
    def __str__ (self):
        return(str("{0:.2f}".format(float(self.x))) + ':' + str("{0:.2f}".format(float(self.y))) + ':' + str("{0:.2f}".format(float(self.z))))
    def __rmul__(self, num):
        return(Vector(self.x * num, self.y * num, self.z * num))


