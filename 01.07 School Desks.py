numberofstudentsA = input("Enter Number of Students in Classroom A: ")
numberofstudentsB = input("Enter Number of Students in Classroom B: ")
numberofstudentsC = input("Enter Number of Students in Classroom C: ")

numberofdesksA = int(numberofstudentsA) // 2
numberofdesksB = int(numberofstudentsB) // 2
numberofdesksC = int(numberofstudentsC) // 2

deskonestudentA = int(numberofstudentsA) % 2
deskonestudentB = int(numberofstudentsB) % 2
deskonestudentC = int(numberofstudentsC) % 2

addedonedeskAll = deskonestudentA + deskonestudentB + deskonestudentC
numberofdesksAllfull = numberofdesksA + numberofdesksB + numberofdesksC
newaddedfulldeskAll = addedonedeskAll // 2
newaddedonedeskAll = addedonedeskAll % 2

totaldesks = str(newaddedonedeskAll + newaddedfulldeskAll + numberofdesksAllfull)
print(str(totaldesks))
