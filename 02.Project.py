
side1= float(input("Enter Side 1: "))
side2= float(input("Enter Side 2: "))
side3= float(input("Enter Side 3: "))

sum= float(side1 + side2+ side3)
halfperimeter= (sum / 2)
x = (halfperimeter*(halfperimeter-side1)*(halfperimeter-side2)*(halfperimeter-side3))
area = (x ** 0.5)
print("{0:.15f}".format(area))
#print(area)