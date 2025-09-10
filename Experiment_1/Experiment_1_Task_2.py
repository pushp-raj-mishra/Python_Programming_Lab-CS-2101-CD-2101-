# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming lab
# Experiment 1 - Task 2: Create a program to compute student marks (average, grade classification)

subjects = int(input("Enter the number of Subjects: "));
marks = 0

# taking marks of all subjects

for i in range(subjects):
    marks += (int(input(f"Enter the Marks in Subject {i+1}:")))

# calculating average

average = marks/subjects
grade = "F" #Initially for no marks, grade is F

# Here we make an if-else tree to check for grades corresponding to the average

if average>=90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Your Average:",average,"\nGrade according to Marks:",grade)

