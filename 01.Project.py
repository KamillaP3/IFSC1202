lengthindays = int(input("Enter Length of Time in Days: "))
lengthinyears = lengthindays // 365
lengthleftoverfromyears = lengthindays % 365
lengthinweeks = lengthleftoverfromyears // 7
lengthleftindays = lengthleftoverfromyears % 7
print("Years: " + str(lengthinyears))
print("Weeks: " + str(lengthinweeks))
print("Days: " + str(lengthleftindays))