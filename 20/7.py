import re

def Format_def(date_str):
    match = re.match(r'(\d{4})-(\d{2})-(\d{2})', date_str)

    if match:
        year, month, day = match.groups()
        new_date_format = f"{day}-{month}-{year}"
        return new_date_format
    else:
        return "Invalid date format"

date_str = '2026-01-02'
converted_date = Format_def(date_str)

print(f"Original date: {date_str}")
print(f"Converted date: {converted_date}")
