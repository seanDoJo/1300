num1 = 0
num2 = 0
fib = 1
length = eval(input("enter the number of sequences: "))
count = 0

print(num1)
while count != length:
	fib += num1
	num1 = num2
	num2 = fib
	count += 1
	print(fib)
