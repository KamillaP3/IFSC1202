lengthraceinkilo = input("Enter Length of Race in Kilometers: ")
minutesneeded = input("Enter Amount in Minutes: ")
secondsneeded = input("Enter Amount in Seconds: ")

fullminutes = int(minutesneeded) + (int(secondsneeded)/60)

fullhours = fullminutes/60
lengthraceinmiles = int(lengthraceinkilo) / 1.61

averagespeedinhours = lengthraceinmiles / fullhours

print("The average speed is " + str(averagespeedinhours) + " per hour")