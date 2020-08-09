import turtle
import math
wn = turtle.Screen()
wn.screensize(800,800)
wn.colormode(255)
sun = turtle.Turtle()
sand = turtle.Turtle()
sky =turtle.Turtle()
ocean = turtle.Turtle()
sunset = turtle.Turtle()
cloud1 = turtle.Turtle()
cloud2 = turtle.Turtle()
cloudcircle1 = turtle.Turtle()
cloudcircle2 = turtle.Turtle



# sand on bottom half of scrseen
wn.bgcolor("#c2b280")




# sky on top half of screen
sky.up()
sky.setpos(-400,-50)
sky.down()
sky.color('#62CFF9','#62CFF9')
sky.begin_fill()
sky.forward(800) 
sky.left(90) 
sky.forward(400)
sky.left(90)
sky.forward(800) 
sky.left(90) 
sky.forward(400)
sky.left(90)
sky.end_fill()

# ocean 
ocean.up()
ocean.setpos(-400, -50)
ocean.down()
ocean.color('#3A85DF','#3A85DF')
ocean.begin_fill()
ocean.forward(800) 
ocean.left(90) 
ocean.forward(100)
ocean.left(90)
ocean.forward(800) 
ocean.left(90) 
ocean.forward(100)
ocean.left(90)
ocean.end_fill()

# sunset ombre 
# sets start position for pen
sunset.up()
yPos = 400
sunset.setposition(-400, yPos)
sunset.down()
# creates variable and sets value to rgb and pensize 
r = 150
g = 95
b = 187
penSize = 15
sunset.pencolor((r,g,b))
sunset.pensize(penSize)
# for loop to change color and y position of pen 
for counter in range(35):
    sunset.speed(10)
    # y position increases by 10 each time
    yPos -= 10
    sunset.setposition(-400, yPos)
    sunset.forward(800)
    # red increases by 1- each time (creates ombre)
    if r < 250:
        r += 5
    sunset.pencolor((r,g,b))

# circle drawing (sun)
sun.up()
sun.setpos(0,100)
sun.down()
sun.begin_fill()
sun.color('orange','yellow')
sun.circle(30)
sun.end_fill()

cloud1.up()
cloud1.setpos(-185, 250)
cloud1.down()
cloud1.pencolor('white')
cloud1.shape("circle") 
#turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
cloud1.shapesize(4,8,0) 
cloud1.fillcolor("white")

#small cloud
x = -200
y = 255
for i in range(11):
    if i == 2:
        x += 40
        y -= 10
    elif i == 3:
        x += 30
        y -= 10
    elif i == 4:
       x += 25
       y -= 20
    elif i == 5:
        x -= 30
        y -= 10
    elif i == 6:
        x -= 40
        y -=10
    elif i == 7:
        x-=40
        y-= 10
    elif i == 8:
        x -=40
        y +=10
    elif i == 9:
        x -+10
        y +=40
    elif i == 10:
        x +=15
        y+=15

    cloudcircle1.up()
    cloudcircle1.setpos(x, y)
    cloudcircle1.down()
    cloudcircle1.begin_fill()
    cloudcircle1.color('white','white')
    cloudcircle1.circle(30)
    cloudcircle1.end_fill()


cloud2.up()
cloud2.setpos(150, 200)
cloud2.down()
cloud2.pencolor('white')
cloud2.shape("circle") 
#turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
cloud2.shapesize(3,6,0) 
cloud2.fillcolor("white")

#big cloud
x = 175
y = 200
for i in range(11):
    if i == 2:
        x += 40
        y -= 10
    elif i == 3:
        x += 30
        y -= 10
    elif i == 4:
       x += 25
       y -= 20
    elif i == 5:
        x -= 30
        y -= 10
    elif i == 6:
        x -= 40
        y -=10
    elif i == 7:
        x-=40
        y-= 10
    elif i == 8:
        x -=40
        y +=10
    elif i == 9:
        x -+10
        y +=40
    elif i == 10:
        x +=15
        y+=15

    cloudcircle1.up()
    cloudcircle1.setpos(x, y)
    cloudcircle1.down()
    cloudcircle1.begin_fill()
    cloudcircle1.color('white','white')
    cloudcircle1.circle(30)
    cloudcircle1.end_fill()
    
turtle.mainloop()


