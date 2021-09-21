import cv2
import numpy as np

#imagenes de carpeta Seq
img_read = cv2.imread('Seq/Img000323.jpg') #Imagen de entrada  
gray_img = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)#Transformamos la imagen de entrada a escala de grises
# Realizar filtrado de mediana, si cambio los valores del filtro me detecta otros circulos pero no me toma los que tomaba antes
img_small = cv2.medianBlur(gray_img, 3)#Esta operación procesa los bordes mientras elimina el ruido, (imagen de entrada,tamaño del kernel) 
img_big = cv2.medianBlur(gray_img, 5)#Esta operación procesa los bordes mientras elimina el ruido, (imagen de entrada,tamaño del kernel)
#Este filtro calcula la mediana de todos los píxeles bajo la ventana del kernel y el píxel central
#se reemplaza con este valor mediano esto es muy efectivo para eliminar el ruido 
rows = img_big.shape[1] #Tomamos el ancho de la imagen procesada 

#parametros de HoughCircles:
#(imagen en un canal gray,metodo a usar,resolucion ,es el umbral más alto para el metodo seleccionado,Valor umbral del acumulador para el método seleccionado,minimo_radio,maximo_radio)
#Circulos Pequeños
small_circles = cv2.HoughCircles(img_small, cv2.HOUGH_GRADIENT, 1.2, 3, param1=30, param2=23, minRadius=8, maxRadius=15)
#Circulos Grandes
big_circles = cv2.HoughCircles(img_big, cv2.HOUGH_GRADIENT, 2.25, rows/64, param1=100, param2=50, minRadius=30, maxRadius=40)
counts_small_circles = 0
#aqui transofrma los datos de las cordenadas y el radio a un int
if small_circles is not None:
    small_circles = np.around(small_circles).astype("int")
    #Recorrido circulos pequeños
    for i in small_circles[0,:]:
        #Dibuja el borde del círculo
        #parametros(imagen,centro,radio,color,grosor del contorno a dibujar)
        cv2.circle(img_read,(i[0], i[1]), i[2], (0,255,255), 2)#dibujamos el contorno del circulo encontrado
        counts_small_circles += 1#contador aumenta 

counts_big_circles = 0
count_blue = 0
count_red = 0
if big_circles is not None:
    big_circles = np.around(big_circles).astype("int")
    #recorrido circulos grandes
    for i in big_circles[0,:]:
        # Dibujar el circulo
        #parametros(imagen,centro,radio,color,grosor del contorno a dibujar)
        cv2.circle(img_read, (i[0], i[1]), i[2], (0,255,0), 2)
        # Obtener el bgr del centro
        b,g,r = img_read[i[1], i[0]]
        if b > r :
            count_blue += 1
        else:
            count_red += 1
        # Dibujar el centro
        cv2.circle(img_read, (i[0], i[1]), 1, (0,0,255), 3)
        counts_big_circles+= 1

    
text_small_circles="Se encontraron: "+ str(counts_small_circles+counts_big_circles)+ " Blobs"+", Small: "+ str(counts_small_circles)+ ", Big: "+ str(counts_big_circles)
text_big_circles=" Blobs Rojo: "+ str(count_red)+ ", Blobs Azul: "+ str(count_blue)
ubication_text_small = (20,290)
ubication_text_big = (20,310)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
letter_size = 0.8
color_letter = (0,0,0)
letter_thickness = 1
cv2.putText(img_read, text_small_circles, ubication_text_small, font, letter_size, color_letter, letter_thickness)
cv2.putText(img_read, text_big_circles, ubication_text_big, font, letter_size, color_letter, letter_thickness)
cv2.imshow("Deteccion de Blob y su cantidad", img_read)
cv2.waitKey()
cv2.destroyAllWindows()
