def calculate():

    # Get input from the user
    num1 = int(input("Enter the first number: "))
    operation = input("Enter the operator (+, -, *, /): ")
    num2 = int(input("Enter the second number: "))

    # Perform the calculation based on the operator
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print(" Division by zero can't proceed.")
            return
        result = num1 / num2
    else:
        print("Invalid")
        return
    
    print(f"{num1} {operator} {num2} = {result}")

calculate()