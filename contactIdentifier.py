#! python3

# Example program, used for US formats

import re, pyperclip

# Create regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
    ((\d\d\d)|(\(\d\d\d)))? # area code (optional)
    (\s|-)                  # first separator
    \d\d\d                  # first 3 digits
    -                       # separator
    \d\d\d\d                # last 4 digits
    ((ext(\.)?\s)|x)        # extension word-part (optional)
    (\d{2,5}))?             # extension number-part (optional)
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