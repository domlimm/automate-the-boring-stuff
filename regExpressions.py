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

bat2Regex = re.compile(r'Bat(wo)?man')
# or 'Bat(wo)?man' 0 or 1 'wo'/s
# or 'Bat(wo)*man' 0 or more 'wo'/s
# or 'Bat(wo)+man' one or more(many) 'wo'/s
mo = bat2Regex.search('The Adventures of Batman')
print(mo.group())
# Batman
mo = bat2Regex.search('The Adventures of Batwoman')
print(mo.group())
# Batwoman

haRegex = re.compile(r'(Ha){3}')
# r'(Ha){3}' -> 3 times
# r'(Ha){3,5}' -> 3-5 times: min-max
print(haRegex.search('He said "HaHaHa"'))
# <re.Match object; span=(9, 15), match='HaHaHa'>

digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('1234567890'))
# <re.Match object; span=(0, 5), match='12345'>
digit2Regex = re.compile(r'(\d){3,5}?')
print(digit2Regex.search('1234567890'))
# <re.Match object; span=(0, 3), match='123'>

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall('First Name: Dom Last Name: Lim'))
# [('Dom', 'Lim')]