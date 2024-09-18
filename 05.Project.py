startrange = int(input("Enter Start of Range: "))
endrange = int(input("Enter End of Range: "))
n = startrange
while n <= endrange:
    number = n
    digits= 0
    newn = n
    while newn > 0:
        newn //= 10
        digits += 1
    newn = n
    sumpowers = 0
    while newn > 0:
        digit = newn % 10
        sumpowers += digit ** digits
        newn //= 10
    if sumpowers == number:
        print(n)
    n+=1

