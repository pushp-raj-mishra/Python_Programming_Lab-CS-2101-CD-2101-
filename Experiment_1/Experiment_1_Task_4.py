# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming lab
# Experiment 1 - Task 4: Input two complex numbers and display their sum, difference, and product

a1 = int(input("Enter the real part of the first complex number: "))
b1 = int(input("Enter the imaginary part of the first complex number: "))
a2 = int(input("Enter the real part of the second complex number: "))
b2 = int(input("Enter the imaginary part of the second complex number: "))

# Sum of complex numbers
sum_real = a1 + a2
sum_imaginary = b1 + b2
print(f"Sum of the complex numbers: {sum_real} + {sum_imaginary}i")

# Difference of complex numbers
diff_real = a1 - a2
diff_imaginary = b1 - b2
print(f"Difference of the complex numbers: {diff_real} + {diff_imaginary}i")

# Product of complex numbers
prod_real = a1 * a2 - b1 * b2
prod_imaginary = a1 * b2 + b1 * a2
print(f"Product of the complex numbers: {prod_real} + {prod_imaginary}i")
