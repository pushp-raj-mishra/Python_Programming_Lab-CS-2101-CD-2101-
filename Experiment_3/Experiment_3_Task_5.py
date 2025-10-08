# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming Lab

# Experiment 3: Task 5: Import the random and math modules. 
# Generate a random number between 1 and 100 using random.randint(). 
# Use the math module to check if the number is prime. 
# (A prime number is a number greater than 1 that has no divisors other than 1 and itself.) 
# Print whether the random number is prime or not.


# importing random and math modules
import random
import math

# to check if a number is prime in sqrt(n) time complexity
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# generating a random number between 1 and 100
random_number = random.randint(1, 100)

# checking if the number is prime and printing the result
if is_prime(random_number):
    print(f"{random_number} is a prime number.")
else:
    print(f"{random_number} is not a prime number.")



# Sample Output: 37 is a prime number.
# Sample Output: 60 is not a prime number.