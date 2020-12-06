# This program says hello, and asks for your name

print('Hello!')
print('What is your name?')
name = input()
print('It is nice to meet you ' + name + '!')
print('Number of characters in your name:')
print(len(name))
print('How old are you?')
age = input()
print('You will be ' + str(int(age) + 1) + ' the next year.')
print('That\'s all! See you again!')