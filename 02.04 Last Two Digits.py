number = float(input("Enter a Number: "))
onedigit= int(number % 10)
tendigit= number / 10
tendigit= int(tendigit % 10) 
tendigit = tendigit *10
lasttwo=tendigit + 0.0 + onedigit
print("{:2.1d}".format(tendigit + onedigit))
