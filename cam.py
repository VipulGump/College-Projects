# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 21:58:39 2020

@author: Sharad Rathi
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()