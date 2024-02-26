import re

def Checker(text):
    pattern = re.compile(r'a-z_')
    match = re.search(pattern, text)

    if match:
        return True
    else:
        return False
    
text1 = 'aab_cbbbc'  # True
text2 = 'aab_Abbbc'  # True
text3 = 'Aaab_abbbc'  # True

result1 = Checker(text1)
result2 = Checker(text2)
result3 = Checker(text3)

print(f"Result for '{text1}': {result1}")
print(f"Result for '{text2}': {result2}")
print(f"Result for '{text3}': {result3}")
