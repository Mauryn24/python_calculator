from decimal import Decimal

class Calculator:
    """A calculator class with support for arbitrary precision arithmetic"""

    def add(self, x, y):
        """Addition operation"""
        return x + y

    def subtract(self, x, y):
        """Subtraction operation"""
        return x - y

    def multiply(self, x, y):
        """Multiplication operation"""
        return x * y

    def divide(self, x, y):
        """Division operation"""
        if y == 0:
            return "Error! Division by zero."
        else:
            return x / y

def main():
    """Main function"""
    calc = Calculator()  # Create an instance of the Calculator class

    print("Welcome to Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = Decimal(input("Enter first number: "))
    num2 = Decimal(input("Enter second number: "))

    if choice == '1':
        result = calc.add(num1, num2)
    elif choice == '2':
        result = calc.subtract(num1, num2)
    elif choice == '3':
        result = calc.multiply(num1, num2)
    elif choice == '4':
        result = calc.divide(num1, num2)
    else:
        print("Invalid choice")
        return

    print("Result:", result)

if __name__ == "__main__":
    main()
