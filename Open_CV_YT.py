# OpenCV com um vídeo do You Tube

import cv2 as cv
import time

cap = cv.VideoCapture('teste.mp4')

if not cap.isOpened():
    print("Error opening video stream or file")
    exit()

while cap.isOpened():
  ret, frame= cap.read()

  if ret == True:
    time.sleep(1/20)
    cv.imshow('frame', frame)
    if cv.waitKey(10) & 0xFF== ord('q'):
      break
  else:
    break

cap.release()
cv.destroyALLWindows()