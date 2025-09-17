# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming lab


# Experiment 1 - Task 1:Create a Python program that asks the user for their age.
# Implement conditional statements to check the following: If the user is below 18, 
# print "You are a minor." If the user is between 18 and 65, print "You are an adult.
# " If the user is above 65, print "You are a senior." 
# Add a check for invalid input (e.g., user enters a non-numeric value).

#Here we are taking the input age
age = input("Enter Your Age: ")

# By default, input is string. We check if the input is non-numeric then it is invalid;
# If input is valid, we typecast it to integer and then proceed with the if-else conditions
if not age.isnumeric():
    print("Invalid Input")
else:
    age = int(age)
    if age < 18:
        print("You are a minor")
    elif age >= 18 and age <= 65:
        print("You are an adult")
    else:
        print("You are a senior")
