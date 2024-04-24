
largest = 0
total = 0
for number in range(10):
	num = int(input('Enter a number: '))
	
	if num > largest:
            largest = num
	
total+= num
	
print(f' the largest number is:{largest}')
