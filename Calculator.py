# Define mathematical operations
def add(x, y):
    """Return the sum of two numbers"""
    return x + y

def subtract(x, y):
    """Return the difference of two numbers"""
    return x - y

def multiply(x, y):
    """Return the product of two numbers"""
    return x * y

def divide(x, y):
   """Return the quotient of two numbers, or an error message if dividing by zero"""
   if y == 0:
        return "Error! Division by zero."
        return x / y

# Main calculator program
def calculator():
    print("Welcome to the Calculator!")
    while True:
        print("\nSelect an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            
            next_calculation = input("Would you like to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                print("Goodbye!")
                break
        else:
            print("Invalid input. Please select a valid operation.")

# Run the calculator
calculator()