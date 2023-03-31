win=0
lose=0
rounds=1
while True:
    import random
    user_rolled = random.randint(1,12)
    user_guess = input("Enter your guess from 1 to 12 or 'q' to quit:")
    if user_guess == 'q':
        rounds+=0
        in_percentage = win/rounds*100
        print("You have played",rounds,"rounds.")
        print("You won",win,"rounds.")
        print("You lose",lose,"rounds.")
        print("Your win percentage is","%.2f"%in_percentage,"%.")
        break
    else:
        rounds+=1
        user_guess = int(user_guess)
        if user_guess == user_rolled:
            win+=1
            print("You win!")
            continue
        else:
            lose+=1
            print("You lose")
        continue