def user_operation():
        """
        '+' for addition,'-' for subtraction,'*' for multipication,'/' for division,'q' for stop,'p' for continue
        """
        while True:
            operation = input("Choose any operation:")
            operation = str(operation)
            if operation == 'q':
                break
            else:
                num1 = int(input("Enter first number:"))
                num2 = int(input("Enter second number:"))
                if operation == '+':
                    sum = num1 + num2
                    print("The sum is",sum)
                elif operation == '-':
                    difference = num1 - num2
                    print("The difference is",difference)
                elif operation == '*':
                    multiple = num1 * num2
                    print("The multiple is",multiple)  
                elif operation == '/':
                    division = num1 / num2
                    print("The division is",division)  
                else:
                    continue
        return
user_operation()
        

