separated1= 0
separated2= 0
separated3= 0
separated4= 0
separated5= 0


for number in range(1,2,5):
	number = int(input('Enter a number: ' ))
	digit1 = number/10000
	digit2 = number% 10000/1000
	digit3 = number % 10000 % 1000/100
	digit4 = number% 10000 % 1000 % 100/10
	digit5 = number% 10000 % 1000 % 1000 %10

	separated1= int(digit1)
	separated2= int(digit2)
	separated3= int(digit3)
	separated4= int(digit4)
	separated5= int(digit5)

	
print(f'{separated1}\t{separated2}\t{separated3}\t{separated4}\t{separated5}')