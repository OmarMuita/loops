import random

num=random.randint(1,10)
print("I shall generate a number from 1 to 10 and you have to guess the number.")
while True:
    guess=int(input("Pick a number:"))
    if guess==num:
        print("You win!")
        break
    else:
        print("Your guess isn't quite right. Try again!")           
