sum=0
print("Enter any postive number less than 100 to do sum. To end, type:a")
while True:
    user_input = input("Enter any number:")
    if user_input == 'a':
            break
    user_input=int(user_input)
    if user_input > 0 and user_input<100:
          sum+=user_input
    else:
          sum+=0     
print(sum)          