
import turtle
import random

def turtle_race(num_turtles):
    turtle.setworldcoordinates(0,0,100,100)
    turtle.delay(0)
    turtle_list = []
    turtle.setpos(90, -100)
    turtle.setpos(90, 200)
    for i in range(num_turtles):
        tr = turtle.Turtle()
        tr.speed(0)
        tr.shape('turtle')
        r = random.random()
        g = random.random()
        b = random.random()
        tr.color(r,g,b)
        tr.penup()
        y = 10 + 80*i/(num_turtles-1)
        tr.setpos(10, y)
        tr.pendown()
        turtle_list.append(tr)
    x = 1
    while x!=0:
      for i in range(len(turtle_list)):
        turtle_list[i].forward(random.randint(1,5))
        if(turtle_list[i].xcor()>90):
          x = 0
          turtle_list[i].turtlesize(3)
          break

turtle_race(10)
