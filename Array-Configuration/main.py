from tkinter import *
from time import *
from math import *

myWindow = Tk()
screen = Canvas( myWindow, width = 600, height = 600, background = "black" )
screen.pack()

n = 500
r = 280

xc = 300
yc = 300

skip = 7
gap = 2 * pi/n
theta = 0

xValues = []
yValues = []
strings = []

for s in range(n):
	x = r * cos(3*theta) + xc
	y = yc - r * cos(5* theta)

	xValues.append(x)
	yValues.append(y)
	strings.append(0)

	screen.create_oval(x-3, y-3, x+3, y+3, fill = "white", outline = "")

	theta = theta + gap 

while True:
	for i in range(n):
		x1 = xValues[i]
		y1 = yValues[i]
		x2 = xValues[(i+skip) % n]
		y2 = yValues[(i+skip) % n]

		strings[i] = screen.create_line(x1, y1, x2, y2, fill = "pink")
		
	skip = skip + 1

	screen.update()
	sleep(0.03)

	for i in range(n):
		screen.delete(strings[i])
	