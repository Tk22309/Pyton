import re
def specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(specific_char("ABCDEFabcdef123450")) 
print(specific_char("*&%@fgfhdfghkhglj#!}{"))

