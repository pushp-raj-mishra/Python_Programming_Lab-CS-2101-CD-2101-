# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming Lab

# Experiment 3: Task 2: Define a function list_summary that accepts a list of integers. 
# Return the sum, average, and maximum value of the list as a tuple. 
# Test the function with a sample list.


def list_summary(integers):
    sum_values = sum(integers) #sum function to calculate sum of list

    average = sum_values/len(integers)

    maximum = max(integers) #max function to calculate maximum of list
    
    return (sum_values,average,maximum)

# Taking input from user
integers = list(map(int,input("Enter the integers: ").split()))

#printing the output
print(list_summary(integers))


# Sample Input: 10 20 30 40 50
# Sample Output: (150, 30.0, 50)

# Sample Input: 5 15 25 35
# Sample Output: (80, 20.0, 35)


