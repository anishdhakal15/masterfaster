from pyfirmata import Arduino,util
import time
b=Arduino('COM4')
def turnonlight():
    b.digital[12].write(1)
    b.digital[11].write(0)

def turnofflight():
    b.digital[12].write(0)

def dooropen():
    b.digital[2].write(1)
    b.digital[6].write(0)
    time.sleep(3)
    b.digital[2].write(0)
def doorclose():
    b.digital[6].write(1)
    b.digital[2].write(0)
    time.sleep(3)
    b.digital[6].write(0)

def fanon():
    b.digital[8].write(1)

def fanoff():
    b.digital[8].write(0)

