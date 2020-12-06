import re

message = 'Call me at +65-9876-5432 tomorrow. or at +65-8765-4321'

phoneNumGrpRegex = re.compile(r'(\+\d\d)-(\d\d\d\d)-(\d\d\d\d)')
mo = phoneNumGrpRegex.search(message)
print(mo.group(1), mo.group(2), mo.group(3))
# +65 9876 5432

phoneNumGrpsRegex = re.compile(r'(\+\d\d)-(\d\d\d\d)-(\d\d\d\d)')
print(phoneNumGrpsRegex.findall(message))
# [('+65', '9876', '5432'), ('+65', '8765', '4321')]

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile popped a tire')
print(mo.group())
# Batmobile
print(mo.group(1))
# mobile