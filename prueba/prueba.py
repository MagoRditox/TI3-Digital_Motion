#Deteccion de Fotos con opencv
import cv2
import numpy as np

img = cv2.imread("lunares.jpg")
imgconvert = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(imgconvert, (5,5), 0)
 
canny = cv2.Canny(gauss, 50, 400) 
cv2.imshow("canny", canny)
cv2.waitKey(0)

(contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("He encontrado {} objetos".format(len(contornos)))
cv2.drawContours(img,contornos,-1,(1,1,1), 2)
cv2.imshow("contornos", img)
cv2.waitKey(0)
