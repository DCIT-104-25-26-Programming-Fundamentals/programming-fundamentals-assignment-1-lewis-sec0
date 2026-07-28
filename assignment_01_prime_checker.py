def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisors from 2 up to sqrt(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


# Main block
number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is NOT a prime number.")