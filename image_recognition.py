import cv2 as cv
import numpy as np
face=cv.CascadeClassifier("man.xml")
cap=cv.VideoCapture(0)
while True:
        rpd,frame=cap.read()
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY) #as this code will work on  gray scale image
        faces=face.detectMultiScale(gray,1.5,2) #
        for (x,y,w,h) in faces:
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv.imshow("img",frame)
        cv.waitKey(0)
