
import random, turtle

class Shape:
  '''
  Purpose: Defines the location of the shape and it's color on the graphic
  Instance variables:
  x: the horizontal position of the shape's center 
  y: the vertical position of the shape's center 
  color: the color of the shape
  Methods:
  __init__ the x and y coordinates, and color of the shape
  __str__ location and the color as a string
  '''
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.color = random.choice(["red", "orange", "yellow", "green", "blue", "purple"])

  def __str__(self):
    loc = "(x="+str(self.x)+", y="+str(self.y)+"), "
    col = self.color
    return loc + col


class Circle(Shape):
  '''
  Purpose: Draws a shape in the turtle graphic with a random color 
  and predetermined size.
  Instance variables: 
  rad - value of the radius of the circle
  Methods: 
  __init__ uses Shape.__init__ values and defines the circles radius
  __str__ returns the type of shape and the radius as a string 
  draw - uses the coordinates and previous arguments to draw a circle 
  with the turtle graphic   
  '''

  def __init__(self, x=0, y=0, rad=0):
    Shape.__init__(self,x,y)
    self.rad = rad

  def __str__(self):
    shape_str = Shape.__str__(self)
    return shape_str + ", rad="+str(self.rad)

  def draw(self,t):
    t.penup()
    t.setpos(self.x,self.y-self.rad)
    t.pendown()
    t.fillcolor(self.color)
    t.begin_fill()
    t.circle(self.rad)
    t.end_fill()

  def contains(self, x, y):
    d = ((x-self.x)**2+(y-self.y-self.rad)**2)**0.5
    return d <= self.rad

class Rectangle(Shape):
  def __init__(self,x=0,y=0,w=0,l=0):
    Shape.__init__(self,x,y)
    self.width = w
    self.length = l
  
  def __str__(self):
    shape_str = Shape.__str__(self)
    return shape_str + ", width = " + str(self.width) + ", length = " + str(self.length)
  
  def draw(self,t):
    t.penup()
    t.setpos(self.x-self.width/2,self.y-self.length/2)
    t.pendown()
    t.fillcolor(self.color)
    t.begin_fill()
    t.forward(self.width)
    t.left(90)
    t.forward(self.length)
    t.left(90)
    t.forward(self.width)
    t.left(90)
    t.forward(self.length)
    t.left(90)
    t.end_fill()

  def contains(self,x,y):
    return (self.x-self.width/2<=x) and (x<=self.x+self.width/2) and (self.y-self.length/2<=y) and (y<=self.y+self.length/2)


class Display:
  '''
  Purpose: To take mouse inputs and use the Shape and Circle classes 
  to draw circles
  Instance variables:
  shapes - defines the shape (a la Circle)
  t - the turtle object being created
  t.speed - instantly draws the entire shape to save time
  t.hideturtle - hides the turtle icon
  shapes.append - creates a new circle
  Methods: __init__ sets up the turtle object's behavior. mouse_event is the response to the click of a mouse on screen.
  '''

  def __init__(self):
    self.shapes = []
    self.t = turtle.Turtle()
    self.t.speed(0)
    self.t.hideturtle()
    turtle.delay(0)
    turtle.onscreenclick(self.mouse_event)
    turtle.listen()
    turtle.mainloop()  #Required for some IDEs

  def mouse_event(self,x,y):
    if Circle.contains(self,x,y) == True:
      return self.__str__(self)
    elif Rectangle.contains(self,x,y) == True:
      return self.__str__(self)
    else:
      n = random.randint(1,2)
      if(n==1):
        new_circ = Circle(x,y,random.randint(10,50))
        self.shapes.append(new_circ)
        new_circ.draw(self.t)
      else:
        new_rect = Rectangle(x,y,random.randint(10,50),random.randint(10,50))
        self.shapes.append(new_rect)
        new_rect.draw(self.t)

Display()
