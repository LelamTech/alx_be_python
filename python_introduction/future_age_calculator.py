from datetime import datetime

# Ask the user for their current age
age = int(input("How old are you? "))

# Calculate years until target year
target_year = 2050
current_year = datetime.now().year
years_to_add = target_year - current_year

# If target year is in the past, inform the user
if years_to_add < 0:
    print(f"{target_year} is already in the past (current year: {current_year}).")
else:
    future_age = age + years_to_add
    print(f"In {target_year}, you will be {future_age} years old.")
