# SmartCalc: A simple console-based calculator
# Provides addition, subtraction, multiplication, division with basic validation

def do_addition(a, b):
    """Return the sum of two numbers"""
    return a + b

def do_subtraction(a, b):
    """Return the difference between two numbers"""
    return a - b

def do_multiplication(a, b):
    """Return the product of two numbers"""
    return a * b

def do_division(a, b):
    """Return the division result, handle division by zero"""
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

def show_menu():
    """Display available calculator options"""
    print("\n" + "-"*45)
    print("              SMART CALCULATOR")
    print("-"*45)
    print("1 ➝ Addition")
    print("2 ➝ Subtraction")
    print("3 ➝ Multiplication")
    print("4 ➝ Division")
    print("5 ➝ Exit Program")
    print("-"*45)

def read_numbers():
    """Take two float inputs safely from the user"""
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        return n1, n2
    except ValueError:
        print("⚠️ Invalid input! Please enter numeric values.")
        return None, None

def calculator():
    history = []  # keeps track of all operations

    while True:
        show_menu()
        option = input("Choose an option (1-5): ")

        if option == "5":
            print("\nExiting SmartCalc... ")
            print("Your session history:")
            for h in history:
                print("  " + h)
            break

        if option not in ["1", "2", "3", "4"]:
            print("Invalid option! Please select 1-5.")
            continue

        x, y = read_numbers()
        if x is None or y is None:
            continue

        if option == "1":
            result = do_addition(x, y)
            operation = "+"
        elif option == "2":
            result = do_subtraction(x, y)
            operation = "-"
        elif option == "3":
            result = do_multiplication(x, y)
            operation = "*"
        elif option == "4":
            result = do_division(x, y)
            operation = "/"

        print(f"\n Result: {x} {operation} {y} = {result}")
        history.append(f"{x} {operation} {y} = {result}")

        again = input("\nDo you want another calculation? (y/n): ").lower()
        if again != "y":
            print("\nGoodbye! Here’s your calculation history:")
            for h in history:
                print("  " + h)
            break

if __name__ == "__main__":
    calculator()
