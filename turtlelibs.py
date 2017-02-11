# -*- coding: utf-8 -*-
import random

# draws letters, length defines how big to draw, x is turtle pen, mult is how far to seperate each letter
def drawh(length, x, mult):
    x.pd()
    x.left(90)
    x.forward(length)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.forward(length * .8)
    x.left(90)
    x.forward(length * .33)
    x.left(90)
    x.forward(length * .8)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.forward(length * 2)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.forward(length * .8)
    x.left(90)
    x.forward(length * .33)
    x.left(90)
    x.forward(length * .8)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.forward(length)
    x.right(90)
    x.pu()
    x.forward(length * mult)

def drawe(length, x, mult):
    x.pd()
    x.left(90)
    x.forward(length)
    x.right(90)
    x.forward(length)
    x.right(90)
    x.forward(length * .4)
    x.right(90)
    x.forward(length * .75)
    x.left(90)
    x.forward(length * .4)
    x.left(90)
    x.forward(length * .75)
    x.right(90)
    x.forward(length * .4)
    x.right(90)
    x.forward(length * .75)
    x.left(90)
    x.forward(length * .4)
    x.left(90)
    x.forward(length * .75)
    x.right(90)
    x.forward(length * .4)
    x.right(90)
    x.forward(length)
    x.right(90)
    x.forward(length)
    x.right(90)
    x.pu()
    x.forward(length * mult)

def drawl(length, x, mult):
    x.pd()
    x.left(90)
    x.forward(length)
    x.right(90)
    x.forward(length * .4)
    x.right(90)
    x.forward(length + (length * .8))
    x.left(90)
    x.forward(length * .6)
    x.right(90)
    x.forward(length * .2)
    x.right(90)
    x.forward(length)
    x.right(90)
    x.forward(length * 1)
    x.right(90)
    x.pu()
    x.forward(length * mult)
    
def drawp(length, x, mult):
    x.pd()
    x.left(90)
    x.forward(length)
    x.right(90)
    x.forward(length)
    x.right(90)
    x.forward(length)
    x.right(90)
    x.forward(length * .66)
    x.left(90)
    x.forward(length)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.forward(length)
    x.right(90)
    x.pu()
    x.forward(length * .33)
    x.left(90)
    x.forward(length * .33)
    x.pd()
    x.forward(length * .33)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.forward(length * .33)
    x.right(90)
    x.pu()
    x.forward(length * .33)
    x.left(90)
    x.forward(length * .33)
    x.left(90)
    x.forward(length * mult)

def gototopleft(x):
    x.pu()
    x.setpos(-935,470)
    x.setheading(0)
    x.pd()


def moveto(x, resx, resy, heading):
    x.pu()
    x.setpos(resx,resy)
    x.setheading(heading)
    x.pd()

#move pen to top left, useful for making square spirals that go inward
    
def innersquare(x):
    x.pu()
    x.setpos(-460,460)
    x.setheading(0)
    x.pd()
    

def spellhehe(length, x, mult):
    drawh(length, x, mult)
    drawe(length, x, mult)
    drawh(length, x, mult)
    drawe(length, x, mult)

def spellhelp(length, x, mult):
    drawh(length, x, mult)
    drawe(length, x, mult)
    drawl(length, x, mult)
    drawp(length, x, mult)

def helpsquare(length, x, mult):
    innersquare(x)
    for i in range (50000):
        spellhelp(length, x, mult)
        spellhelp(length, x, mult)
        spellhelp(length, x, mult)
        spellhelp(length, x, mult)
        spellhelp(length, x, mult)
        spellhelp(length, x, mult)
        spellhelp(length, x, mult)
        spellhelp(length, x, mult)     
        x.right(90.1)
        length = length * .98

def walkingletters(length, x, mult):
    for i in range (50000):
        n = random.randrange(1, 100)
        if 1 <= n <= 25:
            h(length, x, mult)
        elif 26 <= n <= 50:
            e(length, x, mult)
        elif 51 <= n <= 75:
            l(length, x, mult)
        elif 26 <= n <= 100:
            p(length, x, mult)
            x.right(90)

def walkinghehe(length, mult, x, x2, x3):
    coloring(x, x2, x3)
    walker(length, x, mult)
    walker(length, x2, mult)
    walker(length, x3, mult)


def walker(length, x, mult):
    n = random.randrange(1, 50)
    if n <= 10:
        x.left(91)
        x.pu()
        x.forward(length)
        x.pd()
        h(length, x, mult)
    elif 10 <= n <= 25:
        h(length, x, mult)
    elif 26 <= n <= 40:
        e(length, x, mult)
    elif n <= 50:
        e(length, x, mult)
        x.right(91)
        x.pu()
        x.forward(length)
        x.pd()

def earthtones(x):
    rn = random.randrange(0,14)
    if rn == 0:
        x.pencolor('#493829')
    elif rn == 1:
        x.pencolor('#816C5B')
    elif rn == 2:
        x.pencolor('#A8A18C')
    elif rn == 3:
        x.pencolor('#613318')
    elif rn == 4:
        x.pencolor('#755623')
    elif rn == 5:
        x.pencolor('#B99C6B')
    elif rn == 6:
        x.pencolor('#8F3b1B')
    elif rn == 7:
        x.pencolor('#D57500')
    elif rn == 8:
        x.pencolor('#DBCA69')
    elif rn == 9:
        x.pencolor('#404F24')
    elif rn == 10:
        x.pencolor('#668D3C')
    elif rn == 11:
        x.pencolor('#BBD09F')
    elif rn == 12:
        x.pencolor('#4E6172')
    elif rn == 13:
        x.pencolor('#83929F')
    elif rn == 14:
        x.pencolor('#A3ADB8')
    return rn
    
def singlecolor(x, rn):
    if rn == 0:
        x.pencolor('#FFFFFF')
    elif rn == 1:
        x.pencolor('#FDCA40')
    elif rn == 2:
        x.pencolor('#33A1FD')
    elif rn == 3:
        x.pencolor('#F79824')
    elif rn == 4:
        x.pencolor('#27213C')
    elif rn == 5:
        x.pencolor('#5A352A')
    elif rn == 6:
        x.pencolor('#A33B20')
    elif rn == 7:
        x.pencolor('#F4E9C1')
    elif rn == 8:
        x.pencolor('#A0C1B9')
    elif rn == 9:
        x.pencolor('#70A0AF')
    elif rn == 10:
        x.pencolor('#3B1C32')
    elif rn == 11:
        x.pencolor('#CA054D')
    elif rn == 12:
        x.pencolor('#A4D4B4')
    elif rn == 13:
        x.pencolor('#CAD2C5')
    elif rn == 14:
        x.pencolor('#84A98C')
    elif rn == 15:
        x.pencolor('#52796F')
    elif rn == 16:
        x.pencolor('#6B6054')
    elif rn == 17:
        x.pencolor('#FDCA41')
    elif rn == 18:
        x.pencolor('#A1B0AB')
    elif rn == 19:
        x.pencolor('#B8DBD9')
    elif rn == 20:
        x.pencolor('#586F7C')
    elif rn == 21:
        x.pencolor('#2F4550')
    elif rn == 22:
        x.pencolor('#F1FFE7')
    elif rn == 23:
        x.pencolor('#C2E7DA')
    elif rn == 24:
        x.pencolor('#BAFF29')
    elif rn == 25:
        x.pencolor('#EE4266')
    elif rn == 26:
        x.pencolor('#FFD23F')
    elif rn == 27:
        x.pencolor('#3BCEAC')
    elif rn == 28:
        x.pencolor('#D6EFFF')
    elif rn == 29:
        x.pencolor('#FED18C')
    elif rn == 30:
        x.pencolor('#FE654F')
    else:
        x.pencolor('#A1B0AB')
    return rn


def paintingColorsFill(x):
    rn = random.randrange(0,11)
    if rn == 0:
        x.fillcolor('#FFFFFF')
        x.pencolor('#FFFFFF')
    elif rn == 1:
        x.fillcolor('#FFEC00')
        x.pencolor('#FFEC00')
    elif rn == 2:
        x.fillcolor('#C79B00')
        x.pencolor('#C79B00')
    elif rn == 3:
        x.fillcolor('#E34234')
        x.pencolor('#E34234')
    elif rn == 4:
        x.fillcolor("#DC143C")
        x.pencolor("#DC143C")
    elif rn == 5:
        x.fillcolor('#49796b')
        x.pencolor('#49796b')
    elif rn == 6:
        x.fillcolor('#40826D')
        x.pencolor('#40826D')
    elif rn == 7:
        x.fillcolor('#120a8f')
        x.pencolor('#120a8f')
    elif rn == 8:
        x.fillcolor('#0047AB')
        x.pencolor('#0047AB')
    elif rn == 9:
        x.fillcolor('#9C3108')
        x.pencolor('#9C3108')
    elif rn == 10:
        x.fillcolor('#826644')
        x.pencolor('#826644')
    elif rn == 11:
        x.fillcolor('#000000')
        x.pencolor('#000000')

    return rn

def threecolor(x, x2, x3):
    rn = random.randrange(0,30)
    singlecolor(x, rn)
    singlecolor(x2, rn + 1)
    singlecolor(x3, rn + 2)
def followcolor(x, x2, x3, rn):
    singlecolor(x, rn)
    singlecolor(x2, rn + 1)
    singlecolor(x3, rn + 2)

def coloring(x, x2, x3):
    rn = random.randrange(1,100)
    if rn <= 10:
        x.pencolor('#FDCA40')
        x2.pencolor('#33A1FD')
        x3.pencolor('#F79824')
    elif 10 <= rn <= 20:
        x.pencolor('#27213C')
        x2.pencolor('#5A352A')
        x3.pencolor('#A33B20')
    elif 20 <= rn <= 30:
        x.pencolor('#F4E9C1')
        x2.pencolor('#A0C1B9')
        x3.pencolor('#70A0AF')
    elif 30 <= rn <= 40:
        x.pencolor('#3B1C32')
        x2.pencolor('#CA054D')
        x3.pencolor('#A4D4B4')
    elif 40 <= rn <= 50:
        x.pencolor('#CAD2C5')
        x2.pencolor('#84A98C')
        x3.pencolor('#52796F')
    elif 50 <= rn <= 60:
        x.pencolor('#6B6054')
        x2.pencolor('#FDCA40')
        x3.pencolor('#A1B0AB')
    elif 60 <= rn <= 70:
        x.pencolor('#B8DBD9')
        x2.pencolor('#586F7C')
        x3.pencolor('#2F4550')
    elif 70 <= rn <= 80:
        x.pencolor('#F1FFE7')
        x2.pencolor('#C2E7DA')
        x3.pencolor('#BAFF29')
    elif 80 <= rn <= 90:
        x.pencolor('#EE4266')
        x2.pencolor('#FFD23F')
        x3.pencolor('#3BCEAC')
    elif 90 <= rn <= 100:
        x.pencolor('#D6EFFF')
        x2.pencolor('#FED18C')
        x3.pencolor('#FE654F')
        
def setscreens(x, resx, resy):
    x.screensize(resx, resy)
    

def checkLocation(x, height, width):
    xpos = x.xcor()
    ypos = x.ycor()
    if xpos <= (height / -2) or xpos >= (height / 2) or ypos <= (width / -2) or ypos >= (width / 2):
        moveto(x,0,0,0)
        return True
    else:
        return False
