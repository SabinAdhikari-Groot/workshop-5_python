product = 1
num1 = int(input("Enter a number:"))
while num1 != 0:
    num1 = int(input("Enter a number:"))
    if num1 == 0:
        break
    else:
        product*=num1
print("product =",product)    