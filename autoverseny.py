#import Osztály
#t1 = Osztály.Teglalap()
#print("Kerület", t1.kerulet())


#autoverseny
import turtle


def pont():
    print("Pont")
    pass

ablak=turtle.Screen()
ablak.bgcolor("black")
ablak.title("Autóverseny")

ablak.listen()
ablak.onkey(turtle.bye, key="Escape")
ablak.onkey(pont, key="d")

turtle.mainloop()

