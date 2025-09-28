# pattern_drawing.py

# Ask user for size of the pattern
size = int(input("Enter the size of the pattern: "))

# Use a while loop for rows
row = 0
while row < size:
    # Use a for loop for columns
    for col in range(size):
        print("*", end="")
    print()  # move to next line
    row += 1
