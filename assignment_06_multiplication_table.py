def print_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i}  =  {number * i}")


def print_tables_up_to_n(n):
    for num in range(1, n + 1):
        print_table(num)
        print("---------------------------")


# --- Part A: Single Table ---
print("=== Part A: Single Table ===")
number = int(input("Enter a number: "))
print_table(number)

# --- Part B: Bonus - Tables from 1 to N ---
print("\n=== Part B: Tables from 1 to N ===")
n = int(input("Enter a number N: "))

if n <= 0:
    print("Error: N must be a positive integer.")
else:
    print_tables_up_to_n(n)