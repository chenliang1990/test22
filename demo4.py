class GF():
    name = ""
    age = 0
    sanwei = ""
    #构造方法的写法，固定的
    def __init__(self,mz,nl,sw):
        self.name = mz
        self.age = nl
        self.sanwei = sw
gf = GF("林志玲",18,"36D")
print(gf.sanwei)
