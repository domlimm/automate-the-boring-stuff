import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # ['mapit.py', 'address part 1', 'address part 2' ...]
    # -> address part 1 address part 2 ...
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)