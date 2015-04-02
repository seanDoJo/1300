"""
Assignment Name: Assignment 5 - Foxes and Rabbits with Files

Author: Sean Donohoe and Matthew Hurst

Description: This module simulates the population of foxes and rabbits on an island -- using constants for rabbit birth rate, fox birth rate, likelihood a fox and rabbit meet, and probability of success that a fox catches a rabbit -- over a user designated time period, using user-designated starting populations. The data for the ceiling, rounded, raw, and floor values of each day for the foxes and rabbits, along with averages for each will be written to a .csv file.

Date: 9/22/13
"""
import sys
import math
def run_simulation():	
	print()	# adds a newline for nicer output.
	
	initvalues = open("initvals.txt", 'r')
	# rabbit birth rate without predation 
	rbr = float(initvalues.readline())
	#print(rbr)

	# fox birth rate 
	fbr = float(initvalues.readline())
	#print(fbr)

	# INTERACT is the likelihood that a rabbit and fox will meet
	I = float(initvalues.readline())
	#print(I)

	# SUCCESS is the likelihood that when a fox & rabbit meet that the 
	#   fox catches the rabbit
	S = float(initvalues.readline())
	#print(S)
	#exit(0)

	# 1. Gather data from user, one value per input
	foxlr = []
	rabbitlr = [] 

	foxlfl = []
	rabbitlfl = []
	
	foxlceil = []
	rabbitlceil = []

	foxlraw = []
	rabbitlraw = []

	rabbits = eval(input("Enter the starting number of rabbits: "))
	foxes = eval(input("Enter the starting number of foxes: "))
	days = eval(input("Enter the number of days to simulate: "))
	frequency = eval(input("Enter the frequency of days for displaying data: "))

	foxlr.append(round(foxes))
	rabbitlr.append(round(rabbits))

	foxlfl.append(math.floor(foxes))
	rabbitlfl.append(math.floor(rabbits))

	foxlceil.append(math.ceil(foxes))
	rabbitlceil.append(math.ceil(rabbits))

	foxlraw.append(foxes)
	rabbitlraw.append(rabbits)

	roundRabbitsAvg = 0
	roundFoxesAvg = 0

	floorRabbitsAvg = 0
	floorFoxesAvg = 0

	ceilRabbitsAvg = 0
	ceilFoxesAvg = 0

	rawRabbitsAvg = 0
	rawFoxesAvg = 0

	# 2. print out some header info here with labels for days, rabbits, foxes 
	
	#print("\nRoundeds Population Averages:")
	#print("{:9s}{:>10.3f}".format("Rabbits:", roundRabbitsAvg))
	#print("{:9s}{:>10.3f}".format("Foxes:", roundFoxesAvg))

	#displaystr = "{:<10s}{:^20s}{:^19s}{:^20s}{:^29s}".format("", "Rounded Values", "Floor Values", "Ceil Values", "Raw Values")
	#print(displaystr)
	
	#displaystr = "{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>15s}{:>15s}".format("Day", "Rabbits", "Foxes","Rabbits", "Foxes","Rabbits", "Foxes","Rabbits", "Foxes")
	#print(displaystr)
	
	#print("-"*100)

	
	# 3. print out the starting simulation values

	# 4. write a for-loop to iterate through the simulated days
	count = 1
	for i in range(days+1):
		
		F = foxlraw[i]
		R = rabbitlraw[i]	

		Rc = (rbr * R) - (I * R * F)
		Fc = (I * S * R * F) - (fbr * F)

		R += Rc
		F += Fc

		rabbitlraw.append(round(R, 3))
		foxlraw.append(round(F, 3))

		F = foxlr[i]
		R = rabbitlr[i]	

		Rc = (rbr * R) - (I * R * F)
		Fc = (I * S * R * F) - (fbr * F)

		R += Rc
		F += Fc

		rabbitlr.append(round(R))
		foxlr.append(round(F))

		F = foxlfl[i]
		R = rabbitlfl[i]	

		Rc = (rbr * R) - (I * R * F)
		Fc = (I * S * R * F) - (fbr * F)

		R += Rc
		F += Fc

		rabbitlfl.append(math.floor(R))
		foxlfl.append(math.floor(F))

		F = foxlceil[i]
		R = rabbitlceil[i]	

		Rc = (rbr * R) - (I * R * F)
		Fc = (I * S * R * F) - (fbr * F)

		R += Rc
		F += Fc

		rabbitlceil.append(math.ceil(R))
		foxlceil.append(math.ceil(F))
		
	for i in range(days+1):
		roundRabbitsAvg += rabbitlr[i]
		roundFoxesAvg += foxlr[i]

		floorRabbitsAvg += rabbitlfl[i]
		floorFoxesAvg += foxlfl[i]

		ceilRabbitsAvg += rabbitlceil[i]
		ceilFoxesAvg += foxlceil[i]

		rawRabbitsAvg += rabbitlraw[i]
		rawFoxesAvg += foxlraw[i]

	roundRabbitsAvg = roundRabbitsAvg / (days + 1)
	roundFoxesAvg = roundFoxesAvg / (days + 1)

	floorRabbitsAvg = floorRabbitsAvg / (days + 1)
	floorFoxesAvg = floorFoxesAvg / (days+ 1)

	ceilRabbitsAvg = ceilRabbitsAvg / (days + 1)
	ceilFoxesAvg = ceilFoxesAvg / (days + 1)

	rawRabbitsAvg = rawRabbitsAvg / (days +1)
	rawFoxesAvg = rawFoxesAvg / (days + 1)

	filename = input("Enter the name of your file without extensions: ")
	csv = open(filename + ".csv", 'w')
	
	header1 = "Rounded Rabbits Average, Rounded Foxes Average, Floor Rabbits Average, Floor Foxes Average, Ceiling Rabbits Average, Ceiling Foxes Average, Raw Rabbits Average, Raw Foxes Average\n"
	csv.write(header1)
	averages = "%i, %i, %i, %i, %i, %i, %i, %i\n" %(roundRabbitsAvg, roundFoxesAvg, floorRabbitsAvg, floorFoxesAvg, ceilRabbitsAvg, ceilFoxesAvg, rawRabbitsAvg, rawFoxesAvg)
	csv.write(averages)
	
	header2 = "Day, Round Rabbits, Round Foxes, Day, Floor Rabbits, Floor Foxes, Day, Ceiling Rabbits, Ceiling Foxes, Day, Raw Rabbits, Raw Foxes\n"
	csv.write(header2)

	for i in range(0, days+1, frequency):
		csv.write(str(i) + ", ")
		csv.write(str(rabbitlr[i]) + ", ")
		csv.write(str(foxlr[i]) + ", ")
		csv.write(str(i) + ", ")
		csv.write(str(rabbitlfl[i]) + ", ")
		csv.write(str(foxlfl[i]) + ", ")
		csv.write(str(i) + ", ")
		csv.write(str(rabbitlceil[i]) + ", ")
		csv.write(str(foxlceil[i]) + ", ")
		csv.write(str(i) + ", ")
		csv.write(str(rabbitlraw[i]) + ", ")
		csv.write(str(foxlraw[i]) + "\n")

#-----------------------End Assignment 5-----------------------------------------------#
	#print("\nRounded Population Averages:")
	#print("{:9s}{:>10.3f}".format("Rabbits:", roundRabbitsAvg))
	#print("{:9s}{:>10.3f}".format("Foxes:", roundFoxesAvg))

#	print("\nFloor Population Averages:")
#	print("{:9s}{:>10.3f}".format("Rabbits:", floorRabbitsAvg))
#	print("{:9s}{:>10.3f}".format("Foxes:", floorFoxesAvg))
	
#	print("\nCeiling Population Averages:")
#	print("{:9s}{:>10.3f}".format("Rabbits:", ceilRabbitsAvg))
#	print("{:9s}{:>10.3f}".format("Foxes:", ceilFoxesAvg))

#	print("\nRaw Population Averages:")
#	print("{:9s}{:>10.3f}".format("Rabbits:", rawRabbitsAvg))
#	print("{:9s}{:>10.3f}".format("Foxes:", rawFoxesAvg))
#
#
#
#
#	displaystr = "{:<10s}{:^20s}{:^19s}{:^20s}{:^29s}".format("", "Rounded Values", "Floor Values", #"Ceil Values", "Raw Values")
#	print(displaystr)
#	
#	displaystr = "{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>15s}{:>15s}".format("Day", #"Rabbits", "Foxes","Rabbits", "Foxes","Rabbits", "Foxes","Rabbits", "Foxes")
#	print(displaystr)
#	
#	print("-"*100)
#
#	for i in range(0, days+1, frequency):
#		stdoutdump = "{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}{:>15s}{:>15s}".format(str(i), str(rabbitlr[i]), str(foxlr[i]), str(rabbitlfl[i]),str(foxlfl[i]), str(rabbitlceil[i]), str(foxlceil[i]),str(rabbitlraw[i]), str(foxlraw[i]))

#		print(stdoutdump)
		# 5. calculate the new daily populations
	
	
		# 6. print out new day population information   

#	print()	# adds a newline for nicer output. 
#
run_simulation()
