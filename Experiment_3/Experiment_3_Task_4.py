# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming Lab

# Experiment 3: Task 4: Define a function highest_grade that accepts a dictionary 
# with student names as keys and their grades as values. Use the max() function to 
# find the student with the highest grade. 
# Test the function with a sample dictionary.

def highest_grade(grades):
    return max(grades, key=grades.get)

# Taking input from user as dictionary
user_input = input("Enter student names and grades (e.g., A:85 B:90 C:78): ")

#initializing an empty dictionary
grades = {}

# Splitting the input string and building the dictionary
for entry in user_input.split():
    name, grade = entry.split(':')
    grades[name] = int(grade)

print(highest_grade(grades))


# Sample Input: A:85 B:90 C:78
# Sample Output: B

# Sample Input: Pushp:95 Raj:88 Mishra:92
# Sample Output: Pushp