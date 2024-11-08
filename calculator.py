import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x, base=10):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Main function to run the calculator
def scientific_calculator():
    print("Scientific Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    
    while True:
        choice = input("Enter choice (1-10): ")
        
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", power(num1, num2))
        
        elif choice == '6':
            num = float(input("Enter number: "))
            print("Result:", sqrt(num))
        
        elif choice == '7':
            num = float(input("Enter number: "))
            base = float(input("Enter base (default is 10): ") or 10)
            print("Result:", log(num, base))
        
        elif choice in ['8', '9', '10']:
            angle = float(input("Enter angle in degrees: "))
            if choice == '8':
                print("Result:", sin(angle))
            elif choice == '9':
                print("Result:", cos(angle))
            elif choice == '10':
                print("Result:", tan(angle))
        
        else:
            print("Invalid input")
        
        next_calc = input("Do you want to perform another calculation? (yes/no): ")
        if next_calc.lower() != 'yes':
            break

scientific_calculator()
