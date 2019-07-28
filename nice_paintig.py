import turtle
color=["green", "yellow",'orange','blue','pruple','red','pink']
x=10
y= 270
i=0
turtle.bgcolor("black")
while True:
    turtle.color(color[0])
    turtle.forward(x)
    turtle.left(y)
    x+=10
    y-=1
    i+=1
turtle.mainloop()
