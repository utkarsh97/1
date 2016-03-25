"""
your_face.py (5 points)
=====
Draw a face using turtle. For example, you can draw the look of disapproval!

![look of disapproval](http://foureyes.github.io/csci-ua.0002-fall2015-010/resources/img/turtle/your_face.png)

Requirements
-----

* you can draw whatever face you like
* but you have to use the turtle module
    * change the size of the pen 
    * set the window size to 400 x 400
    * turn animation off (for sanity's sake)
* create a function called draw_face ... it's up to you to decide if it should have parameters or not (it's ok if you don't parametrize it, but it may be helpful for extra credit)
    * your function will draw a face
    * use at least one circle
    * use at least one line
    * remember to call update at the end of your function to let Python know to _repaint_ the screen
* call your function at the end of your program

Extra Credit
-----
5 points (warning: this is one may be a little frustrating depending on how complicated your drawing is!)

* ask the user for comma separated input that specifies how to draw the face... with each value representing x, y and size respectively
    * for example, 0,0,20 means draw the face at (0, 0) with size 20
    * size can mean whatever you like... 
* using the string method, split, break up the input, and use each individual value to draw the face
* continue to ask for input, with each new input drawing another face
* hints:
    * how do you keep the relationship between all of the parts of the face in proportion?
    * setheading might be helpful
* see the example below:

![asking for input](http://foureyes.github.io/csci-ua.0002-fall2015-010/resources/img/turtle/your_face_ec.gif)

"""

import turtle
def draw_face(x,y,size):
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setup(400,400)
    wn.tracer(0)
    t.hideturtle()
    t.pensize(size)
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(1, 3):
        t.forward(size*8)
        t.left(135)
        t.forward(size*4)
        t.up()
        t.left(125)
        t.forward(size*3)
        t.right(80)
        t.down()
        t.circle(size*4)
        t.up()
        t.left(90)
        t.forward(size*3)
        t.right(90)
        t.down()
        t.circle(size)
        t.up()
        t.right(180)
        t.goto(x+(size*15), y)
        t.down()
    t.up()
    t.goto(x+(size*10),y-(size*12))
    t.down()
    t.forward(size*4)
    wn.update()

while True:
    answer = input("x,y,size?\n>")
    result = answer.split(',')
    x = int(result[0])
    y = int(result[1])
    size = int(result[2])
    draw_face(x,y,size)
    
