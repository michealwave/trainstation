from turtle import *

t = Turtle()
screen = t.getscreen()
t.speed(0)


name = screen.textinput("name", "What is your name?")
t.write(name, move=True, align="left", font=("Arial", 40, "normal"))
screen.listen()

def go():
	t.forward(10)
	
def right():
	t.right(90)

def left():
	t.left(90)

def penup():
	t.penup()

def pendown():
	t.pendown()

print("Bruh")



screen.onkey(pendown, "P")
screen.onkey(penup, "p")
screen.onkey(left, "Left")
screen.onkey(go, "Up")
screen.onkey(right, "Right")
screen.listen()
screen.mainloop()
