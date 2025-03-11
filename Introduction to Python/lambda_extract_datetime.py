#Write a Python program to extract the year, month, date and time using Lambda. Input: 2020-01-15 09:03:32.744178

"""
Extracts year, month, date, and time from a datetime string and validate the format.
"""

# Lambda function to extract components
extract_datetime = lambda dt_str: {
    "year": int(dt_str[:4]),
    "month": int(dt_str[5:7]),
    "date": int(dt_str[8:10]),
    "time": dt_str[11:]
}
"""Extracts year, month, date, and time from a datetime string."""

# Function to validate datetime format
def is_valid_datetime_format(dt_str):
    """Validates if the input matches 'YYYY-MM-DD HH:MM:SS' format."""
    if len(dt_str) < 19 or not (dt_str[4] == '-' and dt_str[7] == '-' and dt_str[10] == ' ' and dt_str[13] == ':' and dt_str[16] == ':'):
        return False
    try:
        int(dt_str[:4])   # Year
        int(dt_str[5:7])  # Month
        int(dt_str[8:10]) # Date
        int(dt_str[11:13]) # Hour
        int(dt_str[14:16]) # Minute
        float(dt_str[17:]) # Second
        return True
    except ValueError:
        return False

# Main program
if __name__ == "__main__":
    """Prompts user for datetime string, validates, and extracts components."""
    while True:
        datetime_str = input("Enter a datetime string (format: YYYY-MM-DD HH:MM:SS): ").strip()
        
        if is_valid_datetime_format(datetime_str):
            result = extract_datetime(datetime_str)
            print("Extracted Components:")
            for key, value in result.items():
                print(f"{key.capitalize()}: {value}")
            break
        else:
            print("Invalid format. Please enter the datetime string in the format: YYYY-MM-DD HH:MM:SS")