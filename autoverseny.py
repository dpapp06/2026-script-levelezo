#import Osztály
#t1 = Osztály.Teglalap()
#print("Kerület", t1.kerulet())


#autoverseny
import turtle


class Auto(turtle.Turtle):
    def __init__(self, szin, x,y,sebesseg):
        super().__init__()
        self.shape("circle")
        self.color(szin)
        self.penup()
        self.goto(x,y)
        self.sebesseg = sebesseg

    def indit(self):
        self.forward(self.sebesseg)


ablak=turtle.Screen()
ablak.bgcolor("black")
ablak.title("Autóverseny")

a1 =Auto("red", -400,200,15)
a2 =Auto("blue", -400,-200,30)

ablak.listen()
ablak.onkey(turtle.bye, key="Escape")
ablak.onkey(a1.indit, key="d")
ablak.onkey(a2.indit, key="k")

turtle.mainloop()

