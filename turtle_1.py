import turtle

gg = turtle.Turtle()
turtle.bgcolor("pink")

gg.pensize(10)
gg.speed()
gg.forward(120)
gg.right(90)
gg.circle(-150,50)
gg.color("green")
gg.circle(-150,100)
gg.color("yellow")
gg.circle(-150,60)
gg.color("red","red")
gg.begin_fill()
gg.circle(-150,100)
gg.right(90)
gg.forward(50)
gg.right(90)
gg.circle(100,100)
gg.right(90)
gg.forward(50)
gg.end_fill()
gg.begin_fill()
gg.color("yellow","yellow")
gg.right(180)
gg.forward(50)
gg.right(90)
gg.circle(100,60)
gg.right(90)
gg.forward(50)
gg.right(90)
gg.circle(-150,60)
gg.end_fill()
gg.right(90)
gg.forward(50)
gg.right(90)
gg.circle(100,60)
gg.color("green","green")
gg.begin_fill()
gg.circle(100,100)
gg.right(90)
gg.forward(50)
gg.right(90)
gg.circle(-150,100)
gg.right(90)
gg.forward(50)
gg.end_fill()
gg.right(90)
gg.circle(100,100)
gg.color("blue","blue")
gg.begin_fill()
gg.circle(100,25)
gg.left(115)
gg.forward(65)
gg.right(90)
gg.forward(42)
gg.right(90)
gg.forward(124)
gg.right(90)
gg.circle(-150,50)
gg.right(90)
gg.forward(50)
gg.end_fill()

gg.hideturtle()
turtle.done()