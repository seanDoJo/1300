from graphics import *
def main():
	win = GraphWin("Draw yo thang", 680, 700)
	win.setCoords(0.0, 0.0, 20.0, 20.0)
	message = Text(Point(2, 2), "Click away")
	message.draw(win)
	exit = Text(Point(8,8), "Click to exit")
	exit.draw(win)
	check = True
	p = []
	i = 0
	xr = range(7, 11)
	yr = range(7, 10)
	while check == True:
		p[i] = win.getMouse()
		x = p[i].getx()
		y = p[i].gety()
		if x in xr and y in yr:
			exit(0)
		else:
			p[i].draw(win)
	
	
main()
