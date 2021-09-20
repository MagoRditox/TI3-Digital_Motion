import cv2
import numpy as np

img = cv2.imread('Seq/img000046.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
rows = gray.shape[1]

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2.25, rows/64, param1=100, param2=50, minRadius=30, maxRadius=40)

circles = np.uint16(np.around(circles))
cc=0
azul = 0
rojo = 0
for i in circles[0,:]:
    # Dibujar el circulo 
    cv2.circle(img, (i[0], i[1]), i[2], (0,255,0), 2)
    # Obtener el bgr del centro
    b,g,r = img[i[1],i[0]]
    if b>r:
        azul += 1
    else:
        rojo += 1
    # Dibujar el centro
    cv2.circle(img, (i[0], i[1]), 1, (0,0,255), 3)
    cc+= 1
    
text="Se encontraron: "+str(cc)+" Blobs, Rojo: "+str(rojo)+", Azul: "+str(azul)
ubication = (20,310)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
tamañoLetra = 0.8
colorLetra = (0,0,0)
grosorLetra = 1

cv2.putText(img, text, ubication, font, tamañoLetra, colorLetra, grosorLetra)
cv2.imshow('Circulos detectados', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
