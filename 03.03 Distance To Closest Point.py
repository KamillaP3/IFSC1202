a = int(input("Enter Point A: "))
b = int(input("Enter Point B: "))
c = int(input("Enter Point C: "))
x = b - a
y = c - a

if x < 0:
    x = (-x)
else:
    x = x
if y < 0:
    y = (-y)
else:
    y = y

if x <= y:
    print(x)
else:
    print(y)