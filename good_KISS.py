# A good, KISS-based calculator with basic operations
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Undefined"
    return a / b

def square(a):
    return a * a

def square_root(a):
    if a < 0:
        return "Error: Cannot calculate square root of negative number"
    return math.sqrt(a)

def input_numbers():
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input: Please enter a valid number!")
    return a, b

# Main function
def main():
    print("Welcome to the good KISS calculator!")
    while True:
        print("")
        print("Please select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print("6. Square Root")
        print("7. Exit")

        choice = input("Enter your choice: ")

        try:
            choice = float(choice)
        except ValueError:
            print("")
            print("Invalid input: Please enter a number listed above!")
            continue

        if choice == 7:
            print("Thank you for using the calculator. Goodbye!")
            break
        elif choice == 1:
            a, b = input_numbers()
            print("Result: ", add(a, b))
        elif choice == 2:
            a, b = input_numbers()
            print("Result: ", subtract(a, b))
        elif choice == 3:
            a, b = input_numbers()
            print("Result: ", multiply(a, b))
        elif choice == 4:
            a, b = input_numbers()
            print("Result: ", divide(a, b))
        elif choice == 5:
            a, b = input_numbers()
            print("Result: ", square(a))
        elif choice == 6:
            a, b = input_numbers()
            print("Result: ", square_root(a))
        else:
            print("Invalid choice! Please select a number between 1 and 7!")

if __name__ == "__main__":
    main()
