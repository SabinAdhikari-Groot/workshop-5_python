n = input("Enter a two or more digit number:")
max_num = 9
for digits in n:
    digits = int(digits)
    if digits<max_num:
        max_num=digits
print("The smallest digit is",max_num)
