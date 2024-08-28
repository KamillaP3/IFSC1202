number = int(input("Enter a Number: "))
hundreds= number // 100
tens = (number//10) % 10
ones = number % 10

if hundreds < tens < ones:
    print("YES")
else:
    print("NO")