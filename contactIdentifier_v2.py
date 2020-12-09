#! python3

import re, pyperclip

# Create regex for phone numbers
phoneRegex = re.compile(r'''
(
    (((\+)?\d\d))?          # code (optional)
    (\s|-)?                 # first separator
    ((9|8|6)\d\d\d)         # first 4 digits
    (\s|-)?                 # separator
    \d\d\d\d                # last 4 digits
)
''', re.VERBOSE)

# Create regex email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com
[a-zA-Z0-9_.+]+ # name part (range of characters)
@               # @ symbol
[a-zA-Z0-9_.+]+ # domain name part
''', re.VERBOSE)

# Get text off clipboard
text = pyperclip.paste()

# Extract email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []

for phoneNum in extractedPhone:
    allPhoneNumbers.append(phoneNum[0])

# Copy extracted email/phone to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)