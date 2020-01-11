import turtle
def listen(Screen, w, h):
    xbool = False
    ybool = False
    def makeSqaure(x):
        i = 0
        while i<4:
            t.forward(x)
            t.right(90)
            i=i+1
    def makeX(x,y,size):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x+size,y-size)
        t.penup()
        t.goto(x+size,y)
        t.pendown()
        t.goto(x,y-size)
    def makeBoard():
        t.penup()
        t.left(90)
        t.left(90)
        t.forward(50)
        t.right(90)
        t.pendown()
        makeSqaure(150)
        t.penup()
        t.goto(50,0)
        t.pendown()
        t.forward(150)
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.forward(150)
        t.penup()
        t.goto(-50,50)
        t.pendown()
        t.right(90)
        t.forward(150)
        t.penup()
        t.goto(-50,100)
        t.pendown()
        t.forward(150)
        t.penup()
        x = 150
        t.goto(300,x)
        i = 0;
        while i<2:
            t.pendown()
            makeSqaure(50)
            x = x - 50
            t.goto(300,x)
            i=i+1
        makeX(300,150,50)
        t.penup()
        t.goto(325,100)
        t.pendown()
        t.circle(-20)
        t.penup()
        t.goto(300,50)
        t.fillcolor('pink')
        t.pendown()
        t.begin_fill()
        makeSqaure(50)
        t.end_fill()
    def X(x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        makeX(x,y,10)
        t.penup()
        xbool = True
    def O(x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(10)
        t.penup()
        ybool = True
    def button(x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.penup()
        checkerX = None
        checkerO = None
        if t.xcor()>300 and t.xcor()<350 and t.ycor()>100 and t.ycor()<150:
            checkerX = True
            checkerO = False
            window.onscreenclick(X,add=checkerX)
        elif t.xcor()>300 and t.xcor()<350 and t.ycor()>50 and t.ycor()<100:
            checkerY = True
            checkerX = False
            window.onscreenclick(O,add=checkerY)
    t = turtle.Turtle()
    t.speed('fastest')
    makeBoard()
    window.onscreenclick(button)
window = turtle.Screen()
width = 500
height = 500
listen(window,width,height)
window.listen()
window.mainloop()
