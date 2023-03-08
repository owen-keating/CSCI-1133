
# import turtle
# import random

# warm up

# def div27(num):
#     for i in range(2,8):
#         if num % i == 0:
#             divisible = True
#             break
#         else:
#             divisible = False
#     return divisible

# warm up2

# def square(length):
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)

# def spiro(num,length):
#     for i in range(num):
#         turtle.showturtle()
#         r = random.random()
#         g = random.random()
#         b = random.random()
#         turtle.color(r,g,b)
#         turtle.begin_fill()
#         square(length)
#         turtle.end_fill()
#         turtle.left(360/num)

# stretch

# def mul(a,b):
#     total=0
#     for i in range(b):
#         total+=a
#     return total
#
# def mul2(a,b):
#     total=0
#     count=0
#     while(count<b):
#         total+=a
#         count=count+1
#     return total

# stretch2

# def expo(x,y):
#    total=x
#    for i in range(y-1):
#        total*=x
#    return total

# workout

# def walk():
#     turtle.showturtle()
#     for i in range(200):
#         x = 0
#         y = random.randint(1,4)
#         if(y==2):
#             x = 90
#         if(y==3):
#             x = 180
#         if(y==4):
#             x = 270
#         turtle.left(x)
#         turtle.forward(20)

# workout2

# def walk2():
#     turtle.showturtle()
#     count=0
#     while(turtle.xcor()<150 and turtle.xcor()>-150 and turtle.ycor()<150 and turtle.ycor()>-150):
#         x = 0
#         y = random.randint(1,4)
#         if(y==2):
#             x = 90
#         if(y==3):
#             x = 180
#         if(y==4):
#             x = 270
#         turtle.left(x)
#         turtle.forward(20)
#         count+=1
#     turtle.write(count,font=("Arial",20,"normal"))
