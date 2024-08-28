a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a == b and a == c and b == c:
    print(3)
elif b == a or b == c or a == c:
    print(2)
else:
    print(1)