class Desc:
    def __init__(self):
        self.l = None
    def __get__(self,obj,cls):
        if self.l == None:
            self.l = '<' + obj.name + '>'
            return(None)
        else:
            return(self.l)
    def __delete__(self,obj):
        if '<' + obj.name + '>' == self.l:
           self.l = None
    def __set__(self, instance, value):
        self.l = value

class Sem:
    lock = Desc()
    def __init__(self, name):
        self.name = name

 
