import logging

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, \
        format='%(asctime)s - %(levelname)s - %(message)s')
# logging.basicConfig(level=logging.DEBUG, \
#         format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

# Types of logging
# debug, info, warning, error, critical (critical levels)

logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1

    # error was range(n + 1), started at i = 0,
    # that's why everything was 0
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')