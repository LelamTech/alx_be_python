# daily_reminder.py

# Ask user for task, priority, and time-bound flag
task = input("Enter your task for today: ")
priority = input("Enter priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Build reminder based on priority
match priority:
    case "high":
        reminder = f"🔴 HIGH PRIORITY: {task}! Do it as soon as possible."
    case "medium":
        reminder = f"🟠 MEDIUM PRIORITY: {task}. Try to finish it today."
    case "low":
        reminder = f"🟢 LOW PRIORITY: {task}. You can do it when you have extra time."
    case _:
        reminder = f"⚪ Task: {task} (Unknown priority)."

# Add note if time-bound
if time_bound == "yes":
    reminder = reminder + " ⏰ Don't forget it's time-bound!"

print(reminder)
