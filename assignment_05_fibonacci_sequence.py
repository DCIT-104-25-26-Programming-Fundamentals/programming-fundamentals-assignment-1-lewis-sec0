def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def is_fibonacci(num):
    if num < 0:
        return False

    a, b = 0, 1

    while a <= num:
        if a == num:
            return True
        a, b = b, a + b

    return False


# --- Part A: Print the First N Terms ---
print("=== Part A: First N Fibonacci Terms ===")
n = int(input("How many terms? "))

if n <= 0:
    print("Error: N must be a positive integer.")
else:
    sequence = generate_fibonacci(n)
    print("Fibonacci sequence:", " ".join(str(num) for num in sequence))

# --- Part B: Check if a Number Belongs to the Sequence ---
print("\n=== Part B: Check Fibonacci Membership ===")
number = int(input("Enter a number to check: "))

if is_fibonacci(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is NOT a Fibonacci number.")