# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current = datetime.now()
    current_date = current  # save current date into variable as requested
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(days: int):
    today = datetime.now()
    future_date = today + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    display_current_datetime()
    try:
        days_str = input("Enter the number of days to add to the current date: ")
        days = int(days_str.strip())
    except ValueError:
        print("Please enter a valid integer for days.")
        return

    calculate_future_date(days)

if __name__ == "__main__":
    main()
