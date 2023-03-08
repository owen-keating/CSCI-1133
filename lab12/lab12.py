
class Rational:
  def __init__(self,num=0,den=1):
    self.numerator = num
    if den==0:
      self.denominator = 1
    else:
      self.denominator = den
  
  def __str__(self):
    if self.denominator == 1:
      return str(self.numerator)
    else:
      return str(self.numerator) + "/" + str(self.denominator)

class SpaceCoins:
  def __init__(self,pues=0,ninges=0):
    self.p = pues
    self.n = ninges
    if self.n>7 or self.n<0:
      self.p += self.n // 8
      self.n = self.n % 8
  
  def __str__(self):
    if self.p == 0:
      if self.n == 0:
        return "0*"
      else:
        return str(self.n) + "*"
    elif self.n == 0:
      return str(self.p) + "^"
    else:
      return str(self.p) + "^" + str(self.n) + "*"
  
  def __add__(self,other):
    totalp = self.p + other.p
    totaln = self.n + other.n
    return SpaceCoins(totalp,totaln)

  def __sub__(self,other):
    totalp = self.p - other.p
    totaln = self.n - other.n
    return SpaceCoins(totalp,totaln)

class Vec2:
  def __init__(self,x=0,y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return "<{},{}>".format(str(self.x),str(self.y))
  
  def __add__(self,other):
    totalx = self.x + other.x
    totaly = self.y + other.y
    return Vec2(totalx,totaly)
  
  def __mul__(self,scalar):
    totalx = self.x * scalar
    totaly = self.y * scalar
    return Vec2(totalx,totaly)
  
  def get_values(self):
    return [float(self.x),float(self.y)]
  
  def set_values(self,xy):
    self.x = xy[0]
    self.y = xy[1]
