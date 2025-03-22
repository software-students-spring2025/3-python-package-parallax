import random
from datetime import datetime, timedelta

def rand_date_time(current_date_str: str, fortune: str) -> str:
    if not fortune:
        return "Oops: no fortune provided. Please supply a fortune from one of the other functions."
    try:
        current_date = datetime.strptime(current_date_str, "%Y-%m-%d")
    except ValueError:
        return "Oops: Invalid date format. Please use YYYY-MM-DD."
    
    # Year must not exceed 2025.
    if current_date.year > 2025:
        return "Error: The current date cannot be later than the year 2025."
    
    end_date = datetime(2060, 12, 31)
    if current_date > end_date:
        return "Error: The provided date is after the allowed range (December 31, 2060)."
    
    # Calculate a random date between current_date and end_date.
    delta_days = (end_date - current_date).days
    random_offset = random.randint(0, delta_days)
    random_date = current_date + timedelta(days=random_offset)
    
    # Format the random date nicely.
    day_of_week = random_date.strftime("%A")
    month_name  = random_date.strftime("%B")
    day         = random_date.day
    year        = random_date.year

    return f"📅 On {day_of_week}, {month_name} {day}, {year} — {fortune}"