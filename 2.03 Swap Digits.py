number = int(input("Enter a Number: "))
onedigit= (number % 10)
tendigit= number / 10
tendigit= int(tendigit % 10)
newtendigit = onedigit * 10
swappednumber = newtendigit + tendigit
print("{}".format(swappednumber))
