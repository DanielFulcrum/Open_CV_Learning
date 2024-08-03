# Desenhar um retângulo no vídeo #
import cv2 as cv

cap = cv.VideoCapture(0)

width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

#Parte superior
x = width // 2
y = height // 2

#Altura e largura
w = width // 4
h = height // 4

#Parte final: x+w e y+h

while True:
    ret, frame= cap.read() #captura dos frames

    cv.rectangle(frame, (x,y), (x+w, y+h), color= (0, 0, 255), thickness= 4) #Desenho do retângulo

    cv.imshow('frame', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()