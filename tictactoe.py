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
    def O(x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(10)
        t.penup()
    def checkx():
        global check
        check = 'X'
    def checko():
        global check
        check = 'O'
    def button(x,y):
        global check
        t.penup()
        t.goto(x,y)
        t.pendown()
        if t.xcor() > -50 and t.xcor() < 100 and t.ycor() > 0 and t.ycor() < 150:
            if check == 'X':
                X(x,y)
            elif check == 'O':
                O(x,y)
            else:
                print(x,y)
        else:
            print(x,y)
        t.penup()
    t = turtle.Turtle()
    t.speed('fastest')
    makeBoard()
    window.onclick(button)
    window.onkey(checkx,'x')
    window.onkey(checko,'o')
window = turtle.Screen()
width = 500
height = 500
listen(window,width,height)
window.listen()
window.mainloop()
