number = 0
square = 0
cube = 0

print('number\tsquare\tcube')


for number in range(1, 6):
	square = number * number
	cube = number * number * number
	print(f'{number}\t{square}\t{cube}' )