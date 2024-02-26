import re

def Checker(text):
    pattern = re.compile(r'\d$')
    match = pattern.search(text)
    return bool(match)

text1 = 'abcdef'
text2 = 'abcdef6'

result1 = Checker(text1)
result2 = Checker(text2)

print(f"{text1}': {'Yes' if result1 else 'No'}")
print(f"'{text2}': {'Yes' if result2 else 'No'}")
