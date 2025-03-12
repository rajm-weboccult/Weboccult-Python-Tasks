# Python Datetime: Working with dates and times
import datetime
now = datetime.datetime.now()
print(f"Current date and time: {now}")

# Formatting date
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date: {formatted_date}")
