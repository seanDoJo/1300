from graphics import *

def main():
	principal = eval(input("Enter initial principal: "))
	apr = eval(input("Enter interest rate: "))

	win = GraphWin("Investment Growth Chart", 320, 240)
	win.setBackground("white")
	Text(Point(20, 230), ' 0.0k').draw(win)
	Text(Point(20, 180), ' 2.5k').draw(win)
	Text(Point(20, 130), ' 5.0k').draw(win)
	Text(Point(20, 80), ' 7.5k').draw(win)
	Text(Point(20, 30), '10.0k').draw(win)

	height = principal * .02 #.02 pixels per dollar
	bar = Rectangle(Point(40, 230), Point(65, 230-height))
	bar.setFill("green")
	bar.setWidth(2)
	bar.draw(win)

	for year in range(1, 11):
		principal = principal * (1+apr)
		ll = year * 25 + 40
		height = principal * .02
		bar = Rectangle(Point(ll, 230), Point(ll+25, 230-height))
		bar.setFill("green")
		bar.setWidth(2)
		bar.draw(win)

	input("press enter to quit")
	win.close()
	exit(0)
main()
