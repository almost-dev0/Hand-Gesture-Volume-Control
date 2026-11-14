import cv2
import time

wCam, hCam = 640,480            #dimensions of video window

webcam = cv2.VideoCapture(0)
webcam.set(3,wCam)
webcam.set(4,hCam)

while True:
    _ , image = webcam.read()

    cv2.imshow("Hand Gesture Volume Control", image)
    cv2.waitKey(1)