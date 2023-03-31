n = input("Enter a two or more digit number:")
max_num = 0
for digits in n:
    digits = int(digits)
    if digits>max_num:
        max_num=digits
print("The largest digit is",max_num)













