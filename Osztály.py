

class Teglalap:
    szog=90
    def __init__(self,a_oldal:int=5,b_oldal:int=10):
        self.a_oldal=a_oldal
        self.b_oldal=b_oldal

    def terulet(self):
            return(self.a_oldal * self.b_oldal)

    def kerulet(self):
            return 2 * (self.a_oldal + self.b_oldal)


t1 = Teglalap()
print (t1.a_oldal,t1.b_oldal)
print(t1.szog)
print(t1.terulet())
print(t1.kerulet())

t2 = Teglalap(a_oldal=3,b_oldal=8)
print (t2.a_oldal,t2.b_oldal)
print(t2.szog)
print(t2.terulet())
print(t2.kerulet())

