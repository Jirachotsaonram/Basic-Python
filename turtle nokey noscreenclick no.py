import turtle
import random


t = turtle.Turtle()
t.speed(0)
t.width(5)
colors =['red','blue']


def up():
    t.setheading(90) #เป็นที่เปลี่ยนทิศทาง
    t.forward(100) #เป็นคำสั่งเดินหน้า

def down():
    t.setheading(270)
    t.forward(100)

def left():
    t.setheading(180)
    t.forward(100) 

def right():
    t.setheading(0)
    t.forward(100)

def cilckleft(x,y):
    t.color(random.choice(colors))

def cilckright(x,y):
    t.stamp()
 
turtle.listen()

turtle.onscreenclick(cilckleft, 1)
turtle.onscreenclick(cilckright, 3)
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop() #เพื่อให้ระบบทำงานตลอดเวลา
