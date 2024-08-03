# OpenCV com WebCam #

import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error opening video stream or file")
    exit()

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

#Salvando o vídeo
writer = cv.VideoWriter('teste.mp4', cv.VideoWriter_fourcc(*'DIVX'), 20, (width, height))

while True:
  ret, frame= cap.read()

  if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    break

  cv.imshow('frame', frame)
  writer.write(frame)

  if cv.waitKey(1) & 0xFF== ord('q'):
    break

cap.release()
writer.release()
cv.destroyALLWindows()
