import re

message = 'Call me at 9876-5432 tomorrow. or at 8765-4321'

phoneNumRegex = re.compile(r'\d\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(message))