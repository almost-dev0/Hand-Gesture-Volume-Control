import cv2
import time

wCam, hCam = 640,480            #dimensions of video window

webcam = cv2.VideoCapture(0)
webcam.set(3,wCam)                  # property 3 of camera properties, width
webcam.set(4,hCam)                  # property 4 of camera properties, height

pTime = 0

while True:
    # webcam.read returns 2 values, ret and image, ret is whether frame is captured successfully (0/1)
    # we don't need the ret's value, so we keep the variable blank _, indicating we don't need the value
    _ , image = webcam.read()

    # here we calculate frame rate
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # Displaying fps on screen
    # ONLY FIRST FOUR ARGUMENTS ARE REQUIRED HERE
    cv2.putText(image,                        # image input 
                f"FPS : {int(fps)}",          # text
                (20,30),                      # text position
                cv2.FONT_HERSHEY_COMPLEX,     # font
                0.8,                          # font-scale(size)
                (0,0,255),                    # font-color
                2)                            # thickness
    

    cv2.imshow("Hand Gesture Volume Control", image)
    key = cv2.waitKey(1)

    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()