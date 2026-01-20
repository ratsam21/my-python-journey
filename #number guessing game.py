#number guessing game
import random
#sub program
def guess_number(limit,guess):
    number = random.randint(0,limit)
    while guess!= number:
        print("Wrong")
        guess = int(input("What will the number you guess be"))

#main program
limit= int(input("What will the highest number possible be for this number guessing game"))
guess = int(input("What will the number you guess be"))
guess_number(limit,guess)

print("Well done you got it right")