def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        # Get user input for operation
        choice = input("Enter choice (1/2/3/4): ")
        
        # Validate choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid operation.")
            continue
        
        # Get user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Perform calculation based on choice
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "/"

        # Display the result
        if isinstance(result, str):  # If the result is an error message
            print(result)
        else:
            print(f"{num1} {operation} {num2} = {result}")

        # Ask if user wants to perform another calculation
        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != 'yes':
            break

    print("Thank you for using the calculator!")

if __name__ == "__main__":
    main()
