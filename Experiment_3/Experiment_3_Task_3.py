# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming Lab

# Experiment 3: Task 3: Import the datetime module. 
# Define a function get_day_of_week that takes a date string in YYYY-MM-DD format. 
# Use datetime.strptime() to convert the date string into a datetime object and then use strftime('%A') to get the day of the week. 
# Test the function with various dates.


from datetime import datetime

# Function to get the day of the week
def get_day_of_week(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    return date_object.strftime('%A')

date_input = input("Enter the date in YYYY-MM-DD format: ")
print(f"The day of the week for {date_input} is {get_day_of_week(date_input)}")


# Sample Input: 2023-10-05
# Sample Output: Thursday

# Sample Input: 2024-01-01
# Sample Output: Monday