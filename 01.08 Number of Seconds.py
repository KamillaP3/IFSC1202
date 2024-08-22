numberofminutes = input("Enter Number of Minutes: ")
numberofseconds = input("Enter Number of Seconds: ")

numberofminutes = int(numberofminutes) * 60
numberofseconds = int(numberofseconds)

totaltime = int(numberofminutes + numberofseconds)

print("The total number of seconds is: " + str(totaltime))