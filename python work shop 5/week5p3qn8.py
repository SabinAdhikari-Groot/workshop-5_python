import random
random_num = random.randint(1,20)
guessed_times = 0
while True:
    user_input = int(input("Guess a number from 1 to 20:"))
    guessed_times+=1        
    if guessed_times>5:
              print("The random number was",random_num)
              break
    else:
        if user_input == random_num:
            print("You win!")
            break
        elif user_input > random_num:
            print("Guess is high!")
        elif user_input < random_num:
            print("Guess is low!")





                
    
        