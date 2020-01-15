
import turtle
def listen(Screen, w, h):
    #makes a square of length x
    def makeSqaure(x):
        i = 0
        while i<4:
            t.forward(x)
            t.right(90)
            i=i+1
    #makes an 'X' at a specified coordinate and each line had length of size
    def makeX(x,y,size):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.goto(x+size,y-size)
        t.penup()
        t.goto(x+size,y)
        t.pendown()
        t.goto(x,y-size)
    #makes the board
    def makeBoard():
        t.penup()
        t.goto(-300,150)#writes the rule for the game
        t.write('1)press x to place an x',font=("arial",12,"normal"))
        t.goto(-300,125)
        t.write('2)press o to place an o',font=("arial",12,"normal"))
        t.goto(-300,100)
        t.write('3)press q to exit',font=("arial",12,"normal"))
        t.goto(0,0)#start of code that makes the tictactoe board
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
        ystart = 150#loop use to make playagain and undo button
        i = 0
        while i < 2:
            t.goto(300,ystart)
            t.pendown()
            makeSqaure(50)
            t.penup()
            i=i+1
            ystart = ystart - 50
        t.goto(305,125)
        t.write('play again',font=("arial",7,"normal"))
        t.penup()
        t.goto(305,75)
        t.write('Undo',font=("arial",7,"normal"))
    #draws an X
    def X(x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        makeX(x,y,10)
        t.penup()
    #draws an O
    def O(x,y):
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.circle(10)
        t.penup()
    #clears and makes the board again
    def playagain():
        t.clear()
        makeBoard()
    #sents the value of check to x so we know that the user wants to place an X
    def checkx():
        global check
        check = 'X'
    #sents the value of check to o so we know that the user wants to place an O
    def checko():
        global check
        check = 'O'
    #closes the window
    def finish():
        window.bye()
    #undo the users move
    def undo():
        global check
        if check == 'X':#if check equals x then undo 8 times to erase the x
            for i in range(8):
                t.undo()
        elif check == 'O':#if check equals o then undo 4 times to erase the x
            for i in range(4):
                t.undo()
        else:
            print('nothing to undo')
    def button(x,y):
        global check
        t.penup()
        t.goto(x,y)
        t.pendown()
        #if you click in this box playagain
        if t.xcor() > 300 and t.xcor()< 350 and t.ycor() >100 and t.ycor() < 150:
            playagain()
        #if you click this box than its an undo button
        elif t.xcor() > 300 and t.xcor()< 350 and t.ycor() >50 and t.ycor() < 100:
            undo()
        #if x is within this area you can place an x or o
        elif t.xcor() > -50 and t.xcor() < 100 and t.ycor() > 0 and t.ycor() < 150:
            if check == 'X':
                X(x,y)
            elif check == 'O':
                O(x,y)
            else:
                print(x,y)
        else:#print this if user tries to place an x or o not on the board
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
