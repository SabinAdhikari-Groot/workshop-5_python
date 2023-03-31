positive_entered = 0
negative_enterted = 0
zero_entered = 0
print("Enter any postive number or negative number or zero to count. To end, type:a")
while True:
    user_input = input("Enter any number:")
    if user_input == 'a':
            break
    user_input=int(user_input)
    if user_input > 0:
        positive_entered+=1
    elif user_input < 0:
        negative_enterted+=1
    elif user_input == 0:
        zero_entered+=1
print("positive entered:",positive_entered)   
print("negative entered:",negative_enterted)
print("zero_entered:",zero_entered)

























