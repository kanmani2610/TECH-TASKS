class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

def get_operation():
    operations = ['+', '-', '*', '/']
    while True:
        op = input("Enter an operation (+, -, *, /): ")
        if op in operations:
            return op
        print("Invalid operation. Please try again.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

calculator = Calculator()

while True:
    try:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        op = get_operation()

        if op == '+':
            result = calculator.add(num1, num2)
        elif op == '-':
            result = calculator.subtract(num1, num2)
        elif op == '*':
            result = calculator.multiply(num1, num2)
        elif op == '/':
            result = calculator.divide(num1, num2)
        
        print(f"The result is: {result}")
        break

    except ZeroDivisionError:
        print("You can't divide by zero! Please try again.")