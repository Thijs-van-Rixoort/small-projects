import turtle
from random import randint

turtle.hideturtle()
turtle.speed(0)

colorList = ["cyan", "green", "pink", "violet", "blue", "gold", "magenta", "purple", "brown", "orange", "red", "yellow"]
shapeList = ["Circle", "Triangle", "Square", "Pentagon", "Hexagon", "Octagon"]
howManyLayers = randint(1, 10)

def turtleDraw(angle):
    global randomSize
    global howManyShapes

    for i in range(int(360/angle)):
        turtle.right(angle)
        turtle.forward(randomSize)


for i in range(howManyLayers):

    turtle.color(colorList[randint(0, (len(colorList)-1))])
    turtle.width(randint(1, 3))
    randomSize = randint(25, 250)
    howManyShapes = randint(6, 36)
    howManyShapes -= (howManyShapes%6)
    drawShape =  shapeList[randint(0, (len(shapeList)-1))]

    for i in range(howManyShapes):
        turtle.circle(30, (360/howManyShapes), 1)
        
        if drawShape == "Circle":
            turtle.circle(randomSize)

        elif drawShape == "Triangle":
            turtleDraw(120)

        elif drawShape == "Square":
            turtleDraw(90)

        elif drawShape == "Pentagon":
            turtleDraw(72)

        elif drawShape == "Hexagon":
            turtleDraw(60)

        elif drawShape == "Octagon":
            turtleDraw(45)
        

turtle.Screen().exitonclick()