#program to take pictures useing rapberry pie via python programing
import os #import os libraries
import time#import time libraries
a=0
b=1
while a<=10:#while statement

    t="fswebcam -F 5 --fps 20 -r \"1200x800\" /home/pi/cam/imgs/"+str(b)+".jpg"
    os.system(t)
    print(b)
    a=a+1
    b=b+1
    time.sleep(30)# time diffrence
