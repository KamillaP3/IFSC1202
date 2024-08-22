numberofhoursfirst = input("Enter Number of Hours in First Timestamp: ")
numberofminutesfirst = input("Enter Number of Minutes in First Timestamp: ")
numberofsecondsfirst = input("Enter Number of Seconds in First Timestamp: ")
numberofhourssecond = input("Enter Number of Hours in Second Timestamp: ")
numberofminutessecond = input("Enter Number of Minutes in Second Timestamp: ")
numberofsecondssecond = input("Enter Number of Seconds in Second Timestamp: ")

numberofhoursfirst = int(numberofhoursfirst) * 3600
numberofminutesfirst= int(numberofminutesfirst) * 60
numberofsecondsfirst = int(numberofsecondsfirst)
totaltimestamp = int(numberofhoursfirst + numberofminutesfirst + numberofsecondsfirst)

numberofhourssecond = int(numberofhourssecond) * 3600
numberofminutessecond = int(numberofminutessecond) * 60
numberofsecondssecond = int(numberofsecondssecond)
totaltimestampsecond = int(numberofhourssecond + numberofminutessecond + numberofsecondssecond)

secondsbetween = (totaltimestampsecond - totaltimestamp)

print("The number of seconds between the first and second timestamp is " + str(secondsbetween))