def factorial(n):
	num = 1
	for i in range(1, n + 1):
		num = num * i
	return num

userinput = int(input("Number please: "))
userinput = factorial(userinput)
print(userinput)