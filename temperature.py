temperature = float(input("Enter the temperature"))

if temperature >= 70:
	print("the weather exteremly")
elif temperature > 40 and temperature < 70:
	print("the weather is hot")
elif temperature > 20 and temperature < 40:
	print("the weather is average")
elif temperature >= 1 and temperature <= 20:
	print("the weather is cold")
	print("go out with your sweater")

else:

	print("the weather is exteremly cold,stay home")
