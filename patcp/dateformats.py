import datetime

current_date = datetime.date.today()
print("Current date:", current_date)

specific_date = datetime.date(2023, 5, 15)
print("Specific date:", specific_date)

current_time = datetime.datetime.now().time()
print("Current time:", current_time)

parsed_date = datetime.datetime.strptime("2023-05-15 10:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed_date)

print("\nDifferent Date Formats:")

now = datetime.datetime.now()

print("1. Year (4-digit):", now.strftime("%Y"))  # 4-digit year
print("2. Short Year (2-digit):", now.strftime("%y"))  # 2-digit year
print("3. Month (Numeric):", now.strftime("%m"))  # Month as a number (01-12)
print("4. Month (Abbreviation):", now.strftime("%b"))  # Month as an abbreviation
print("5. Month (Full Name):", now.strftime("%B"))  # Month as full name
print("6. Day of Month:", now.strftime("%d"))  # Day of the month (01-31)
print("7. Day of Week (Abbreviation):", now.strftime("%a"))  # Day as an abbreviation
print("8. Day of Week (Full Name):", now.strftime("%A"))  # Day as full name

print("\nDifferent Time Formats:")

print("1. Hour (24-hour format):", now.strftime("%H"))  # Hour (00-23)
print("2. Hour (12-hour format):", now.strftime("%I"))  # Hour (01-12)
print("3. Minute:", now.strftime("%M"))  # Minute (00-59)
print("4. Second:", now.strftime("%S"))  # Second (00-59)
print("5. Microsecond:", now.strftime("%f"))  # Microsecond (000000-999999)
