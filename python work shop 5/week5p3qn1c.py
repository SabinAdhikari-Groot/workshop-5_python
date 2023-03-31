sum=0
print("Enter any postive number less than 100 to do sum.")
while True:
    user_input = int(input("Enter any number:"))
    if user_input > 0:
          sum+=user_input
          if user_input > 100:
                break
          if user_input < 100:
                continue      
print(sum)          




