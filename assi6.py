"""
This program draws a picture using the graphics module.

Author: Sean Donohoe
Assignment 6
"""
from graphics import *

def __init__():
	win = GraphWin("Sean's Drawing", 680, 700)
	win.setCoords(0.0, 0.0, 30.0, 30.0)
	start = Text(Point(4,29), "Click to make him mad")
	start.draw(win)
	win.setBackground("white")
	#win.getMouse()
	drawable(win)

def eyeball():
	pupil = Oval(Point(14,21),Point(15.5, 18))
	pupil.setFill("black")
	glint = Oval(Point(14.17, 20.5), Point(14.5, 19.6))
	glint.setFill("white")
	outside = Oval(Point(13.5,21.7), Point(16,17))
	outside.setFill("white")
	return pupil, glint, outside

def body():
	c = color_rgb(46, 255, 139)
	#mainbod = Oval(Point(11, 23), Point(19, 8))
	#mainbod.setFill("green")
	squareb = Rectangle(Point(11, 23), Point(18.5, 8))
	squareb.setFill(c)
	squareb.setOutline(c)
	topc = Circle(Point(14.75, 23), 3.75)
	topc.setFill(c)
	topc.setOutline(c)
	bottomc = Circle(Point(14.75, 8), 3.75)
	bottomc.setFill(c)
	bottomc.setOutline(c)
	return squareb, topc, bottomc

def eyebrow(x, y):
	c = "black"
	t1p1 = Polygon(Point(x, y), Point(10.9, 22.8), Point(11.1, 24.3), Point(x+.1,y+1.2))
	t1p1.setFill(c)
	t1p2 = Polygon(Point(x, y), Point(18.7, 23), Point(18.4,24.5), Point(x+.1,y+1.2))
	t1p2.setFill(c)
	return t1p1, t1p2

def antenna():
	a1o = Circle(Point(19.7, 24), 4)
	a1i = Circle(Point(20.1, 23.8), 4)
	a1o.setFill("black")
	a1i.setFill("white")
	a1i.setOutline("white")
	a2o = Circle(Point(9.8, 24), 4)
	a2i = Circle(Point(9.4, 23.8), 4)
	a2o.setFill("black")
	a2i.setFill("white")
	a2i.setOutline("white")
	return a1o, a1i, a2o, a2i
def cheeks(val):
	c1 = Circle(Point(16.9, 16), 1)
	c1.setFill(val)
	c1.setOutline(val)
	c2 = Circle(Point(12.3, 16), 1)
	c2.setFill(val)
	c2.setOutline(val)
	return c1, c2
def mouth(x, y):
	m1 = Circle(Point(14.75, 13), 2)
	m1.setFill("white")
	return m1

def drawable(window):
	win = window
	out, inc, out1, inc1 = antenna()
	out.draw(win)
	inc.draw(win)
	out1.draw(win)
	inc1.draw(win)
	bod, t, b = body()
	b.draw(win)
	t.draw(win)
	bod.draw(win)
	m1 = mouth(1, 2)
	m1.draw(win)
	c1, c2 = cheeks(color_rgb(46, 255, 139))
	c1.draw(win)
	c2.draw(win)
	pl1, gl, out = eyeball()
	out.draw(win)
	pl1.draw(win)
	gl.draw(win)
	eyeb1, eyeb2 = eyebrow(14.75, 23.8)
	eyeb1.draw(win)
	eyeb2.draw(win)
	y = 23.8
	xc = 46
	yc = 255
	zc = 139
	win.getMouse()
	for i in range(0, 8):
		x = 14.75
		y = y - .4
		eyeb1.setFill(color_rgb(46, 255, 139))
		eyeb2.setFill(color_rgb(46, 255, 139))
		eyeb1.setOutline(color_rgb(46, 255, 139))
		eyeb2.setOutline(color_rgb(46, 255, 139))
		eyeb1, eyeb2 = eyebrow(x, y)
		xc = xc + 26.13
		yc = yc - 31.9
		zc = zc - 17.4
		c1, c2 = cheeks(color_rgb(xc,yc,zc))
		c1.draw(win)
		c2.draw(win)
		eyeb1.draw(win)
		eyeb2.draw(win)
		win.getMouse()
	win.getMouse()

__init__()
