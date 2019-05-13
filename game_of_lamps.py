# 矩阵灯的 问题

# # 定义二维list的方法
# LampSquare = [[0 for i in range(2)] for i in range(2)]
import turtle

LampSquare = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
LampSquareCursorX, LampSquareCursorY = 0, 0
LampSquareLampX, LampSquareLampY = 0, 0
LampSquareLevel = 0


def LampSquareButtonDraw():
    turtle.goto(-200, -150)
    turtle.color('black', 'green')
    turtle.pendown()
    turtle.begin_fill()
    turtle.fd(60)
    turtle.right(90)
    turtle.fd(20)
    turtle.right(90)
    turtle.fd(60)
    turtle.right(90)
    turtle.fd(20)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-200 + 5, -150 - 18)
    turtle.write('set levels', font=('Arial', 10, 'normal'))


def LampSquareDraw(square):
    turtle.penup()
    turtle.goto(-200, 200)
    for tempx in range(len(square)):
        turtle.goto(-200, 200 - 30 * tempx)
        for tempy in square[tempx]:
            if tempy == 0:
                turtle.color('black', 'gray')
            else:
                turtle.color('black', 'yellow')
            turtle.pendown()
            # turtle.dot
            turtle.begin_fill()
            turtle.fd(20)
            turtle.right(90)
            turtle.fd(20)
            turtle.right(90)
            turtle.fd(20)
            turtle.right(90)
            turtle.fd(20)
            turtle.right(90)
            turtle.end_fill()
            turtle.penup()
            turtle.fd(30)


def LampSquareClickCursorGet(clickx, clicky):
    global LampSquareCursorX, LampSquareCursorY
    LampSquareCursorX, LampSquareCursorY = clickx, clicky
    # print(LampSquareCursorX, LampSquareCursorY)
    # turtle.goto(clickx, clicky)
    LampSquareClickCallback()


def LampSquareClickCallback():
    # button
    if -200<LampSquareCursorX<-140 and -170<LampSquareCursorY<-150:
        LampSquareButtonAct()
    # lamp square
    global LampSquareLampX, LampSquareLampY
    LampSquareLampX, LampSquareLampY = \
        LampSquareClickLampGet(LampSquareCursorX, LampSquareCursorY, LampSquare)
    newSquare = LampSquareCal(LampSquareLampX, LampSquareLampY, LampSquare)
    # print(LampSquareLampX, LampSquareLampY)
    turtle.tracer(False)
    LampSquareDraw(newSquare)
    turtle.update()
    turtle.tracer(True)
    return


def LampSquareClickLampGet(clickx, clicky, square):
    if clickx < -200 or clickx > -200 + 30*len(square):
        return -1, -1
    if clicky > 200 or clicky < 200 - 30*len(square):
        return -1, -1
    if (clickx - -200) % 30 > 20:
        return -1, -1
    if (200 - clicky) % 30 > 20:
        return -1, -1
    squarey = int((clickx - -200) / 30)
    squarex = int((200 - clicky) / 30)
    return squarex, squarey


def LampSquareCal(squarex, squarey, square):
    if squarex == -1 or squarey == -1:
        return square
    square[squarex][squarey] = not square[squarex][squarey]
    if squarex > 0:
        square[squarex - 1][squarey] = not square[squarex - 1][squarey]
    if squarex < len(square) - 1:
        square[squarex + 1][squarey] = not square[squarex + 1][squarey]
    if squarey > 0:
        square[squarex][squarey - 1] = not square[squarex][squarey - 1]
    if squarey < len(square) - 1:
        square[squarex][squarey + 1] = not square[squarex][squarey + 1]
    return square


def LampSquareInputLevel():
    global LampSquareLevel
    tempLevel = int(turtle.numinput('Levels', 'input square levels(3-10)'))
    if tempLevel < 3 or tempLevel > 10:
        # turtle.goto(-230, 200)
        # turtle.pencolor('red')
        # turtle.write('invalid number, please input again.',
        #              font=('Arial', 20, 'normal'))
        LampSquareInputLevel()
    else:
        LampSquareLevel = tempLevel


def LampSquareButtonAct():
    global LampSquare
    LampSquareInputLevel()
    LampSquare = [[0 for i in range(LampSquareLevel)]
                  for i in range(LampSquareLevel)]
    turtle.tracer(False)
    turtle.clear()
    LampSquareDraw(LampSquare)
    LampSquareButtonDraw()
    turtle.update()
    turtle.tracer(True)


if __name__ == '__main__':
    # init
    turtle.setup(500, 500)
    turtle.speed(0)
    turtle.pensize(1)
    turtle.penup()
    turtle.hideturtle()
    # input levels
    LampSquareInputLevel()
    LampSquare = [[0 for i in range(LampSquareLevel)]
                  for i in range(LampSquareLevel)]
    # display lamps
    turtle.tracer(False)
    LampSquareDraw(LampSquare)
    LampSquareButtonDraw()
    turtle.update()
    turtle.tracer(True)
    # lamp click event
    turtle.onscreenclick(LampSquareClickCursorGet)
    turtle.done()
    turtle.mainloop()