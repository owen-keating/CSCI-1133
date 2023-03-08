
import turtle
import math
import random

class Lander:
  def __init__(self,xpos,ypos,xvel,yvel):
    '''
    Purpose: (What does an object of this class represent?)
    Instance variables: (What are the instance variables for   
    this class, and what does each represent in a few words?)
    Methods: (What methods does this class have, and what does 
    each do in a few words?)
    '''
    turtle.Turtle.__init__(self)
    self.x = xpos
    self.y = ypos
    self.vx = xvel
    self.vy = yvel
    self.fuel = 50
    self.left(90)
    self.forward(20)
