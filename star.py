import turtle
# import time install turtle by pip

col=('yellow','green','cyan','pink','white','violet','indigo','red','orange')

t=turtle.Turtle()
t.width(3)
screen=turtle.Screen()
screen.bgcolor('violet')
t.speed(0)

x=1

for i in range(35):
    for j in range(0,4):
        t.color(col[(0+i+j)%9])
        t.fd(x)
        t.lt(45)
        t.color(col[(1+i+j)%9])
        t.fd(x)
        t.rt(90)
        t.color(col[(2+i+j)%9])
        t.fd(x)
        t.lt(45)
        t.color(col[(3+i+j)%9])
        t.fd(x)
        t.rt(90)
    t.lt(135)
    t.up()
    t.fd(10)
    t.down()
    t.rt(135)
    x=x+4

t.up()
t.goto(-425,-80)
t.down()
t.pencolor('blue')
t.write("THANK YOU!",align='left',font=("Comic Sans MS",100,'bold'))
t.hideturtle()

# time.sleep(10)
turtle.done()
