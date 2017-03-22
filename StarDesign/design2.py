from myfunction import *
import turtle
# This function should create four stars near each other 
bob=turtle.Turtle()
alice=turtle.Turtle()
carl=turtle.Turtle()
rick=turtle.Turtle()
turtle.bgcolor("black")
# This should change the background color to black

bob.speed(0)
alice.speed(0)
carl.speed(0)
rick.speed(0)
# This changes the speed of the turtles

turtle.colormode(255)

#bob.begin_fill()
bob.width(5)
bob.pu()
bob.goto(-200,0)
bob.pd()
# This should change the width and tell the turtle to move to a certain place 
for times in range(256):
    c=(times, 0, 0)
    bob.color(c)
    print(c)
    polygon(bob, 1, 150)
    bob.left(150)
    bob.forward(times)
#bob.end_fill()
# This makes a red star on the left using a loop

    
#alice.begin_fill()
alice.width(5)
alice.pu()
alice.goto(200,0)
alice.pd()
for times in range(256):
    c=(times, times, times)
    alice.color(c)
    print(c)
    polygon(alice, 1, 150)
    alice.left(150)
    alice.forward(times)
#alice.end_fill()
# This makes a white star on the right using a loop
    
#carl.begin_fill()
carl.width(5)
carl.pu()
carl.goto(0,200)
carl.pd()
for times in range(256):
    c=(0, 0, times)
    carl.color(c)
    print(c)
    polygon(carl, 1, 150)
    carl.left(150)
    carl.forward(times)
#carl.end_fill()
# This makes a blue star at the top using a loop


#rick.begin_fill()
rick.width(5)
rick.pu()
rick.goto(0,-200)
rick.pd()
for times in range(256):
    c=(0, 0, times)
    rick.color(c)
    print(c)
    polygon(rick, 1, 150)
    rick.left(150)
    rick.forward(times)
#rick.end_fill
# This makes another blue star at the bottom using a loop

