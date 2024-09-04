firstnumber = input("Enter First Number: ")
secondnumber = input("Enter Second Number: ")
thirdnumber = input("Enter Third Number: ")

if firstnumber < secondnumber and secondnumber < thirdnumber:
    print(firstnumber + ", " + secondnumber + ", " + thirdnumber)
elif secondnumber < firstnumber and firstnumber < thirdnumber:
     print(secondnumber + ", " + firstnumber + ", " + thirdnumber)
elif firstnumber < thirdnumber and thirdnumber < secondnumber:
        print(firstnumber + ", " + thirdnumber + ", " + secondnumber)
elif secondnumber < thirdnumber and thirdnumber < firstnumber:
         print(secondnumber + ", " + thirdnumber + ", " + firstnumber)
elif thirdnumber < secondnumber and secondnumber < firstnumber:
        print(thirdnumber + ", " + secondnumber + ", " + firstnumber)
else:
      print(thirdnumber + ", " + firstnumber + ", " + secondnumber)

 
