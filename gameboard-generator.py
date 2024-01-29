import turtle

turtle.hideturtle()
turtle.speed(100)

bordtype = int(input("Grootte van het bord: "))
riblengte = 25
x = 0
y = 0

def row():
  global bordtype
  
  for i in range(bordtype):
    square()
    
def square():
  global x
  global riblengte
  
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(riblengte)
    turtle.right(90)
  turtle.end_fill()
  turtle.forward(riblengte)
  if x % 2 == 1:
    turtle.color("black")
    x = 0
  else:
    turtle.color("white")
    x += 1

for i in range(bordtype):
  row()
  turtle.penup()
  if y % 2 == 1:
    turtle.right(90)
    if i != bordtype - 1:
        turtle.forward(riblengte * 2)
    else:
        turtle.forward(riblengte)
    turtle.right(90)
    y = 0
  else:
    turtle.left(180)
    y += 1
  turtle.pendown()

turtle.color("black")
for i in range(4):
    turtle.forward(riblengte * bordtype)
    if y == 1:
        turtle.left(90)
    else:
        turtle.right(90)

turtle.Screen().exitonclick()