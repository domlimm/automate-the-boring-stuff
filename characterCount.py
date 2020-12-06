# 'pprint' module for pretty printing of Dictionaries

message = 'It was a bright cold day in December, and the clock was striking fourteen.'
count = {} # Dictionary to hold key val pairs

for char in message.upper():
    if char not in count:
        count.setdefault(char, 1)
    else:
        count[char] += 1

print(count)