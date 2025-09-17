# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming Lab

# Experiment 2: Write a program to validate a password based on the following criteria:
# Minimum 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one number
# At least one special character (e.g., @, #, !, etc.)
# Use a while loop to repeatedly ask for a password until a valid one is entered. 
# Use decision-making to give feedback to the user about which criteria were not met.

while True:
    # Taking Input
    password = input("Enter Your Password: ")

    # Checking Minimum Length Criteria
    has_min_len = len(password) >= 8

    # Checking if an uppercase character is present
    has_upper = any(c.isupper() for c in password)

    # Checking if a lowercase character is present
    has_lower = any(c.islower() for c in password)

    # Checking if a digit is present
    has_digit = any(c.isdigit() for c in password)

    # Checking if a special character is present.
    # Here we also check that the special character is not whitespace
    has_special = any((not c.isalnum()) and (not c.isspace()) for c in password)

    if all([has_min_len, has_upper, has_lower, has_digit, has_special]):
        print("Password is Valid!")
        break
    else:
        print("Invalid Password. Missing criteria:")
        if not has_min_len:
            print("- Must be at least 8 characters long")
        if not has_upper:
            print("- Must contain at least one uppercase letter")
        if not has_lower:
            print("- Must contain at least one lowercase letter")
        if not has_digit:
            print("- Must contain at least one digit")
        if not has_special:
            print("- Must contain at least one special character (@, #, !, etc.)")
        print("Please try again.\n")


