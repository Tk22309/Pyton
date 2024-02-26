import re

def find_pitona(text1):
    pattern = re.compile(r'python', re.IGNORECASE)
    matches = pattern.findall(text1)
    return matches

text1 = 'Python kuchma pYthoN vova pythOn genadiy PYTHOn'
result = find_pitona(text1)
print(result)

