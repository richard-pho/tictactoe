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
        t.goto(-300,150)
        t.write('1)press x to place an x',font=("arial",12,"normal"))
        t.goto(-300,125)
        t.write('2)press o to place an o',font=("arial",12,"normal"))
        t.goto(-300,100)
        t.write('3)press q to exit',font=("arial",12,"normal"))
        t.goto(0,0)
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
        t.goto(300,150)
        t.pendown()
        makeSqaure(50)
        t.penup()
        t.goto(305,125)
        t.write('play again',font=("arial",7,"normal"))
        t.goto(300,100)
        t.pendown()
        makeSqaure(50)
        t.penup()
        t.goto(305,75)
        t.write('Undo',font=("arial",7,"normal"))
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
    def playagain():
        t.clear()
        makeBoard()
    def checkx():
        global check
        check = 'X'
    def checko():
        global check
        check = 'O'
    def finish():
        window.bye()
    def button(x,y):
        global check
        t.penup()
        t.goto(x,y)
        t.pendown()
        if t.xcor() > 300 and t.xcor()< 350 and t.ycor() >100 and t.ycor() < 150:
            playagain()
        elif t.xcor() > -50 and t.xcor() < 100 and t.ycor() > 0 and t.ycor() < 150:
            if check == 'X':
                X(x,y)
            elif check == 'O':
                O(x,y)
            else:
                print(x,y)
        else:
            print("place x or o on the board")
        t.penup()
    t = turtle.Turtle()
    t.speed('fastest')
    makeBoard()
    window.onclick(button)
    window.onkey(checkx,'x')
    window.onkey(checko,'o')
    window.onkey(finish,'q')
window = turtle.Screen()
width = 500
height = 500
listen(window,width,height)
window.listen()
window.mainloop()
