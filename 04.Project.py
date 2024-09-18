#start = int(input("Enter Start of Range:"))
#end = int(input("Enter End of Range:"))

#for i in range (start, end + 1):
    # if start % i == 0:
      #  print(i)
    
#def prime:
#    if n <= 1:
#        return False
 #   for i in range(2, (n // 2) + 1):
 #       if n % i == 0:
 #           return False
 #   return True


startrange = int(input("Enter Start of Range: "))
endrange = int(input("Enter End of Range: "))

n=startrange, endrange + 1

#print("Prime Numbers between" + startrange + "and" + endrange + ":")

for i in range(startrange, endrange + 1):
   if n % i == 0:
       print(n)
   # if prime(i):
       # print(i)