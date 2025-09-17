# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming Lab


# Experiment_2: Task 5: Create a list of sales data for the past 12 months (e.g., sales figures in thousands). 
# Calculate the total sales, average sales, and the month with the highest sales using loops. 
# Use matplotlib to plot the monthly sales and highlight the month with the highest sales.

# Sales data (in thousands)
sales_data = [25, 32, 29, 35, 41, 40, 45, 38, 50, 55, 60, 70]

# Calculate total sales using loop
total_sales = 0
for sales in sales_data:
    total_sales = total_sales + sales

# Calculate average sales
average_sales = total_sales / len(sales_data)

# Find month with highest sales using loop
highest_sales = sales_data[0]
highest_month = 0
for i in range(len(sales_data)):
    if sales_data[i] > highest_sales:
        highest_sales = sales_data[i]
        highest_month = i

# Here we are calculating total, average and month with highest sales
print(f"Total sales: {total_sales}")
print(f"Average sales: {average_sales}")
print(f"Month with highest sales: {highest_month + 1} (${highest_sales}k)")

# Plotting using matplotlib
import matplotlib.pyplot as plt

months = list(range(1, 13))

plt.plot(months, sales_data)
plt.plot(highest_month + 1, highest_sales, 'ro', markersize=8)
plt.show()