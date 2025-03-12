"""
Write a Python program that takes two numbers, start and end, and prints all prime numbers in that range.

Example:
  For start = 10, end = 30:
  11, 13, 17, 19, 23, 29
"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Implementation in Python

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=", ")

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

print(f"Prime numbers between {start} and {end}:")
print_primes(start, end)


Output-
Enter start number: 50
Enter end number: 70
Prime numbers between 50 and 70:
53, 59, 61, 67,
