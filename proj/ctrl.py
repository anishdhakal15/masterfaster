from pyfirmata import Arduino,util
import time
b=Arduino('COM4')
def turnonlight():
    b.digital[13].write(1)

def turnofflight():
    b.digital[13].write(0)

def turndoor(stop):
    while(True):
        b.digital[13].write(1)
        time.sleep(0.2)
        b.digital[13].write(0)
        time.sleep(0.7)
        b.digital[13].write(1)
        time.sleep(0.3)
        b.digital[13].write(0)
        time.sleep(0.7)
        if stop():
            break

def fanon():
    b.digital[8].write(1)

def fanoff():
    b.digital[8].write(0)

