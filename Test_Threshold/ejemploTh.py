import cv2
import numpy as np  
image = cv2.imread('circulos.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(gray, 200,255, cv2.THRESH_BINARY_INV)

contornos, jQ= cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      
cv2.drawContours(image, contornos, -1, (0,255,0),3)
print('Total de circulos:',len(contornos))  
cv2.imshow('imagen',image)
cv2.imshow('th', th)
cv2.waitKey(0)
cv2.destroyAllWindows()