import re

"""

Assignment Name: Assignment 3 - Interest Calculator

Author: Sean Donohoe

Description: This module calculates interest over a user-designated time period using an interest rate and starting amount, also designated by the user

Date: 9/5/2013

"""
#futval.py
#	A program to compute the value of an investment
#	carried 10 years into the future

def main():
	print("This program calculates the future value\nof a user-designated investment")

	timei = eval(input("Enter the number of years you wish to assess: "))
	principal = eval(input("Enter your initial principal: "))
	interest = input("Enter the interest rate in the form of N.NN%\ne.g. 42.3%\nEnter annual your interest rate[%]: ")
	periods = eval(input("Enter the number of compound periods per year: "))

	aprs = re.sub('%', '', interest)
	apri = float(aprs)
	aprf = apri/periods
	apr = aprf/100
	#print(apr) --debug tool

	time = timei * periods

	looper = loop(time, principal, apr)
	#print("looper main():", looper) --debug tool
	return looper

def loop(count, principal, apr):
	track = 0
	apr = apr + 1
	while track != count:
		track += 1
		principal = principal * apr
		#print(principal) --debug tool
	print(principal)
	#exit(0)
	check = input("Would you like to calculate again? [y/n]: ")
	if check == "Y" or check == "y":
		looper = True
	else:
		looper = False
	#print("looper loop:", looper) --debug tool
	return looper

	
looper = True
while looper == True:
	looper = main()
	#print("looper final:", looper) --debug tool
exit(0)
