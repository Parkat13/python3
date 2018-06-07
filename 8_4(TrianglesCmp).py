import math
class Triangle:
    def __init__(self, x, y, z):
        if x < y + z and y < x + z and z < x + y and x > 0 and y > 0 and z > 0:
            self.flag = 1
        else:
            self.flag = -1
        self.x, self.y, self.z = float(x), float(y), float(z)
    def __abs__(self):
        if self.flag == -1:
            return(0)
        else:
            p = (self.x + self.y + self.z)/2.0
            return(math.sqrt(p*(p-self.x)*(p-self.y)*(p-self.z)))
    def __lt__(self, other):
        return(abs(self) < abs(other))
    def __gt__(self, other):
        return(abs(self) > abs(other))
    def __le__(self, other):
        return(abs(self) <= abs(other))
    def __ge__(self, other):
        return(abs(self) >= abs(other))
    def __eq__(self, other):
        l1 = [self.x, self.y, self.z]
        l2 = [other.x, other.y, other.z]
        l1.sort()
        l2.sort()
        for i in range(3):
            if l1[i] != l2[i]:
                break
        else:
            return(True)
        return(False)
    def __str__(self):
        return (str(self.x) + ':' + str(self.y) + ':' + str(self.z))
    def __bool__(self):
        if self.flag == 1:
            return(True)
        else:
            return(False)

