
total = 0
passed = 0
failed = 0	


while True:
	number = int(input("Enter a number : "))

	if number == 1:
		passed = passed + 1
	if number == 2:
		failed = failed + 1
	if number > 2:
		break
total += number
print(f" passed is: {passed}")
print(f" failed is: {failed}")

	
