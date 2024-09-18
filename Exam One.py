name = str(input("Hello! What is your name? "))
print("Well, "+ name,", I am thinking of a number between 1 and 20.")
print("You have 5 guesses.")
from random import randint
x = randint(1,20)
for guesses in range(1,6):
    guess1 = int(input("Take a guess: "))
    if guess1 > x:
         print("Your guess is too high.")
    elif guess1 < x:
          print("Your guess is too low.")
    else:


        print("Good job,", name, "! You guessed my number in", guesses, "guesses!")
        break

else:
    computernumber = str(x)
    print("Nope. The number I was thinking of was " + computernumber)
