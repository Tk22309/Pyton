import re

def Checker(text_list):
    result = []
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    for text in text_list:
        matches = re.findall(pattern, text)
        result.extend(matches)
    
    return result

texts = ['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 'abc111@test.com']

result = Checker(texts)
print(result)
