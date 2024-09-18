startrange = int(input("Enter Start of Range: "))
endrange = int(input("Enter End of Range: "))

start=str(startrange)
end=str(endrange)
n=startrange, endrange + 1
print("Prime Numbers between " + start + " and " + end + ": ")

for n in range(startrange, endrange + 1):
   if n > 1:
       prime= True
       for i in range(2, n // + 1):
            if n % i == 0:
             prime= False
       if prime == True:
          print(n)
