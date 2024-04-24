
total = 1
average = 0
product = 1
smallest = 2000000000
largest = 0
num = 1

for num in range(1,5):
	number = int(input("Enter a number: " ))
	
	if number > largest:
		largest = number


	if number < smallest:
		smallest = number

	total+= number	
	average = total / num
	product*= number


print(f" largest is: {largest}")
print(f" smallest is: {smallest}")
print(f" average is: {average}")
print(f" product is: {product}")


