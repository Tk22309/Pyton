import re

def Checker(ip):
    pattern = r'\b0+(\d+)\b'
    result = re.sub(pattern, r'\1', ip)
    return result


ip_address = "216.08.094.196"
new_ip = Checker(ip_address)

#result = ip.replace('0', '')
print(new_ip)
