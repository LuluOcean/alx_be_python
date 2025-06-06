from datetime import datetime, timedelta

def display_current_date():
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    print(f"Date {days} days from now: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")


days = int(input("Enter number of days to add to current date: "))
display_current_date()
calculate_future_date(days)