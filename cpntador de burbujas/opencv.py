import cv2
import numpy as np

#imagenes de carpeta Seq
img_read = cv2.imread(r'Img000006.jpg')
gray_img= cv2.cvtColor(img_read,cv2.COLOR_BGR2GRAY)
# Realizar filtrado de mediana, si cambio los valores del filtro me detecta otros circulos pero no me toma los que tomaba antes
img = cv2.medianBlur(gray_img,3)

"""circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,1,param1=30,param2=30,minRadius=8,maxRadius=15)   circles2 = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,1,param1=30,param2=23,minRadius=8,maxRadius=15)"""
circles2 = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1.2,3,param1=30,param2=23,minRadius=8,maxRadius=15)
#sin error img 8 circles2 = circles2 = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1.2,3,param1=30,param2=23,minRadius=8,maxRadius=15)

#aqui transofrma los datos de las cordenadas y el radio a un int
"""
circles = np.uint16(np.around(circles))
count = 0
for i in circles[0,:]:
    #Dibuja el borde del círculo
    cv2.circle(img_read,(i[0],i[1]),i[2],(0,255,255),2)
    count = count + 1"""

circles2 = np.uint16(np.around(circles2))
count = 0
for i in circles2[0,:]:
    #Dibuja el borde del círculo
    cv2.circle(img_read,(i[0],i[1]),i[2],(0,255,255),2)
    count = count + 1


text="Se encontraron: "+str(count)+" Blobs"
ubication = (20,310)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
tamañoLetra = 0.8
colorLetra = (0,0,0)
grosorLetra = 1

cv2.putText(img_read, text, ubication, font, tamañoLetra, colorLetra, grosorLetra)
cv2.imshow("Deteccion de Blob y su cantidad",img_read)
cv2.waitKey()
cv2.destroyAllWindows()
