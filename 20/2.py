import re

def check_b_after_a(text):
    pattern = r'a(b{2,})'
    match = re.search(pattern, text)
    
    if match:
        return True
    else:
        return False

text1 = "ab"
text2 = "aabbbbbc"

result1 = check_b_after_a(text1)
result2 = check_b_after_a(text2)

print(f"Result for '{text1}': {result1}")
print(f"Result for '{text2}': {result2}")
