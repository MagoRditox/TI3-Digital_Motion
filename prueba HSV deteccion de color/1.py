#Deteccion de Fotos con opencv
import cv2
import numpy as np
# Diferenciar entre colores y seleccionar cada contorno correspondiente
 
img = cv2.imread("1.1.PNG")
imgconvert = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#Determinar rangos de colores 
#Se definen 2 rojos debido a que existen 2 rangos uno al inicio y otro al final
redlow1 = np.array([0,100,20],np.uint8)
redhigh1 =np.array([10,255,255],np.uint8)
redlow2 = np.array([175,100,20],np.uint8)
redhigh2 =np.array([100,255,255],np.uint8)
bluelow = np.array([110,100,20],np.uint8)
bluehigh = np.array([130,255,255],np.uint8)

#Se definen las mascaras a utilizar para identificacion de color
maskblue = cv2.inRange(imgconvert,bluelow,bluehigh)
maskred1 = cv2.inRange(imgconvert,redlow1,redhigh1)
maskred2 = cv2.inRange(imgconvert,redlow2,redhigh2)
maskred = cv2.add(maskred1,maskred2)

#Draw contorns

conred = cv2.findContours(maskred,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
cv2.drawContours(img,conred,-1,(0,255,0),2)
conblue = cv2.findContours(maskblue,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
cv2.drawContours(img,conblue,-1,(0,255,255),2)

#Mostramos por pantalla

cv2.imshow("Original",img)
cv2.imshow('MaskRed',maskred)
cv2.imshow("Imagen", imgconvert)
cv2.waitKey(0)
cv2.destroyAllWindows()
