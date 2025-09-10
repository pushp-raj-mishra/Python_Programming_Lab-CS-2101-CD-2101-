# Student Name: Pushp Raj
# Roll Number: 2024UG3016
# Course: CS-2101/CD-2101 - Python Programming lab
# Experiment 1 - Task 5: Convert temperature from Celsius to Fahrenheit and vice versa

# Get choice from user
choice = input("Enter 'C' to convert Celsius to Fahrenheit or 'F' to convert Fahrenheit to Celsius: ").strip().upper()

if choice == 'C':
    temperature_celsius = float(input("Enter temperature in Celsius: "))
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {temperature_fahrenheit}°F")
elif choice == 'F':
    temperature_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    temperature_celsius = (temperature_fahrenheit - 32) * 5/9
    print(f"Temperature in Celsius: {temperature_celsius}°C")
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
