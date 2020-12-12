def createBox(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol needs to have only 1 character.')

    if width < 2 or height < 2:
        raise Exception('Width/Height must be greater or equals to 2.')

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

def logging():
    import traceback

    try:
        raise Exception('This is the error message.')
    except:
        logFile = open('log.txt', 'a')
        logFile.write(traceback.format_exc())
        logFile.close()
        print('Logged in log.txt')

createBox('*', 10, 2)
logging()