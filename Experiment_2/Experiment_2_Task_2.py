# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming Lab

# Experiment 2: Task 2: Write a Python program that generates a multiplication table for numbers from 1 to 12. 
# Use nested loops to display the table in a well-formatted way. 
# Print both the rows and columns of the table with their appropriate labels.

# We keep the range of numbers here, so we can easily change numbers according to our requirements
table_from = 1
table_upto = 12

multiplication_from = 1
multiplication_upto = 10

for i in range (table_from, table_upto+1): # We will write tables of these numbers
    
    print(f"Multiplication Table of {i}")  #Heading for following table
    
    for j in range (multiplication_from, multiplication_upto+1): #Table will go here
    
        print(f"{i} X {j} =",i*j)


