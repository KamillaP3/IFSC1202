number = int(input("Enter a Number: "))
onedigit= (number % 10)
tendigit= number / 10
tendigit= int(tendigit % 10)
print("{}".format(onedigit))
print("{}".format(tendigit))