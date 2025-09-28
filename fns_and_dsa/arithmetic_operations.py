# calculator.py

# Step 1: Define the function
def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"

# Step 2: Take user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Choose operation (add/subtract/multiply/divide): ").lower()

# Step 3: Call the function
result = perform_operation(num1, num2, operation)

# Step 4: Print result
print("Result:", result)
