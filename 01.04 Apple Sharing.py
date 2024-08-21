numberofstudents = input("Number of Students: ")
numberofapples = input("Number of Apples: ")
numberofstudents = int(numberofstudents)
numberofapples = int(numberofapples)
applesperstudent = (numberofstudents // numberofapples)
print("Each student will get " + str(applesperstudent) + " apples")
leftoverapples = numberofstudents % numberofapples
print("There will be " + str(leftoverapples) + " apples leftover")