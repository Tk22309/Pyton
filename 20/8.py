import re

def find_all_phones(text):
    pattern = re.compile(r'\+\d{3}\(\d{2}\)\d{3}-\d{1,3}-\d{3,4}')
    matches = pattern.findall(text)
    return matches

text = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'

result = find_all_phones(text)
print(result)
