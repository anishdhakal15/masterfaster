import vision as vctrl
import threading
a=[7]
#hd = threading.Thread(target = vctrl.humandetect, args =(lambda : a, ))
while(True):
    #hd.start()
    x=vctrl.humandetect()
    print(x)
    if x:
        print("detected")
    #hd.join()