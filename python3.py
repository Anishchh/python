# task1_math_operations.py

# Step 1: Take input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division safely
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Step 3: Display the results
print("\nResults:")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
