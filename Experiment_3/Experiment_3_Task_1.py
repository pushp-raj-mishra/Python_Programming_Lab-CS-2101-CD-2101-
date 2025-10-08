# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming Lab

# Experiment 3: Task 1: Define a function rectangle_area_perimeter that takes the length and width as input parameters. 
# Return both the area and perimeter of the rectangle from the function. 
# Call the function with different sets of length and width values. 

def rectangle_area_perimeter(length, width):
  area = length * width #area of rectangle
  perimeter = 2 * (length + width) #perimeter of rectangle
  return (area, perimeter)

# Taking input from user
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

print(rectangle_area_perimeter(length,width))


# Sample Input: 5 10
# Sample Output: (50, 30)

# Sample Input: 7 3
# Sample Output: (21, 20)
