def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def show_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


# Main block
symbols = {
    "1": "+",
    "2": "-",
    "3": "*",
    "4": "/",
    "5": "%",
    "6": "**"
}

while True:
    show_menu()
    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4", "5", "6"):
        print("Error: Invalid choice. Please enter a number between 1 and 7.")
        print()
        continue

    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)
        if result is None:
            print("Error: Cannot divide by zero.")
            print()
            continue
    elif choice == "5":
        result = modulus(a, b)
    elif choice == "6":
        result = exponent(a, b)

    print(f"Result: {a} {symbols[choice]} {b} = {result}")
    print()def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def show_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


# Main block
symbols = {
    "1": "+",
    "2": "-",
    "3": "*",
    "4": "/",
    "5": "%",
    "6": "**"
}

while True:
    show_menu()
    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4", "5", "6"):
        print("Error: Invalid choice. Please enter a number between 1 and 7.")
        print()
        continue

    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)
        if result is None:
            print("Error: Cannot divide by zero.")
            print()
            continue
    elif choice == "5":
        result = modulus(a, b)
    elif choice == "6":
        result = exponent(a, b)

    print(f"Result: {a} {symbols[choice]} {b} = {result}")
    print()def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def show_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


# Main block
symbols = {
    "1": "+",
    "2": "-",
    "3": "*",
    "4": "/",
    "5": "%",
    "6": "**"
}

while True:
    show_menu()
    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break

    if choice not in ("1", "2", "3", "4", "5", "6"):
        print("Error: Invalid choice. Please enter a number between 1 and 7.")
        print()
        continue

    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))

    if choice == "1":
        result = add(a, b)
    elif choice == "2":
        result = subtract(a, b)
    elif choice == "3":
        result = multiply(a, b)
    elif choice == "4":
        result = divide(a, b)
        if result is None:
            print("Error: Cannot divide by zero.")
            print()
            continue
    elif choice == "5":
        result = modulus(a, b)
    elif choice == "6":
        result = exponent(a, b)

    print(f"Result: {a} {symbols[choice]} {b} = {result}")
    print()