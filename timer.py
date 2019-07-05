import time
#### START MEASURING TIME ####
start=time.time()

import logging
# https://docs.python.org/2/howto/logging.html

import datetime
import sys
print("\n\nSTARTING: ",datetime.datetime.now(),"\n")
#from datetime import date
#from datetime import datetime

#logging.basicConfig(filename='timer.py.log',level=logging.INFO, format='%(asctime)s.%(msecs)03d %(levelname)s:\t%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('timer.py.log', mode='a')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

logger = setup_custom_logger('myapp')
message = (start, " start working")
logger.info(message)

a = input('\ndescribe the work you are doing:\n\n')
logger.warning(a)


b = input('\nhit enter to STOP timer\n\n')

#log = logging.getLogger("MyApp")

stop=time.time()
message = (stop, " stop working")
logger.info(message)
secondsWorked= stop - start
hoursWorked=(round(secondsWorked/3600,4))
print("ENDING: ",datetime.datetime.now(),"\n\n")
print(hoursWorked,"\n\n")
message = (hoursWorked,'hours worked')
logger.info(message)
message = (secondsWorked,'seconds worked')
logger.info(message)
time.sleep(10)
