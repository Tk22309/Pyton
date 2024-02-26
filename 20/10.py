import re

def sanitize_phone_number(phone_numbers):
    cleaned_numbers = [re.sub(r'[()+\s-]', '', number) for number in phone_numbers]
    return cleaned_numbers

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

result = sanitize_phone_number(phone_numbers)
for number in result:
    print(number)
