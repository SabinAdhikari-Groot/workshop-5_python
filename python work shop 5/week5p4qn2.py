import random
user_rolled = random.randint(1,12)
while True:
    user_guess = int(input("Enter your guess from 1 to 12:"))
    if user_guess == user_rolled:
        print("You win!")
        break
    else:
        continue





