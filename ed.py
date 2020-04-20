import turtle 

ed = turtle.Turtle()
ed.shape('turtle')
ed.color('pink')
ed.speed(1)

# Letter "Y"
ed.left(135)
ed.penup()
ed.goto(-320, 320)
ed.right(135)

ed.right(45)
ed.pendown()
ed.goto(-270, 270)

ed.right(45)
ed.goto(-270, 170)

ed.penup()
ed.left(180)
ed.goto(-270, 270)

ed.right(45)
ed.pendown()
ed.goto(-220, 320)


# Letter "o"
ed.penup()
ed.goto(-170, 170)

ed.right(45)
ed.pendown()
ed.circle(50)


# Letter "u"
ed.penup()
ed.goto(-100, 270)

ed.right(90)
ed.pendown()
ed.forward(50)
ed.circle(50, 180)
ed.forward(50)


# Letter "a"
ed.penup()
ed.goto(-320, 80)

ed.pendown()
ed.right(180)
ed.circle(50, -180)

ed.goto(-220, 0)

ed.goto(-295, 0)
ed.right(90)
ed.circle(25, -180)

ed.goto(-220, 50)

# Letter "r"
ed.penup()
ed.goto(-200, 0)

ed.pendown()
ed.goto(-200, 80)
ed.left(90)
ed.circle(50, -180)


# Letter "e"
ed.penup()
ed.goto(-80, 80)

ed.pendown()
ed.goto(20, 80)
ed.circle(50, 180)

ed.goto(-80, 50)
ed.circle(50, 180)





#Letter "y"
ed.penup()
ed.goto(-110, -30)

ed.pendown()
ed.right(180)
ed.circle (40, -180)
ed.penup()
ed.goto(-110, -30)

ed.pendown()
ed.goto(-110, -130)
ed.right(180)
ed.circle(20, -180)

#Letter "h"
ed.penup()
ed.goto(-310, -150)
ed.left(180)
ed.pendown()
ed.goto(-210, -150)








turtle.done()
