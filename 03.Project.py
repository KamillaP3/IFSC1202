firstnumber = float(input("Enter First Number: "))
operator = input("Enter Operator (+,-.*,/): ")
secondnumber = float(input("Enter Second Number: "))
if operator == "+" :
    print((firstnumber + secondnumber))
elif operator == "-":
    print((firstnumber - secondnumber))
elif operator == "*" :
    print((firstnumber * secondnumber))
elif operator == "/" :
    print((firstnumber / secondnumber))
else:
        print("Invalid Operator")
