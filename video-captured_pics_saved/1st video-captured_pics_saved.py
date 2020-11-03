import cv2
import numpy as np
import os

cap=cv2.VideoCapture(0)
a=0

#using loop because capturing frame by frame
while(True):
        
        path="F:\Study\Python\OpenCV\start\Video opencv programs\pics"
        ret,frame=cap.read()     #capture frame by frame
        
        #convert captured frames to gray  
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        #show gray frames
        cv2.imshow('FRAME',gray)
        #saving all frames with different name heloo1,2,3,4........jpg 
        cv2.imwrite(os.path.join(path,'heloo'+str(a)+'.jpg'),gray)
        a+=1

        if cv2.waitKey(1) & 0xFF==ord('q'):
                break

cap.release()
cv2.destroyAllWindows()
