import cv2
import numpy as np
import time
promedio = float(0)
dividido = float(0)

for k in range (0,1212,1):

    try:
        if k < 10 and k >=0:
            Imagen = 'Seq/Img00000'+str(k)+'.jpg'
        if k < 100 and k >=10:
            Imagen = 'Seq/Img0000'+str(k)+'.jpg'
        if k < 1000 and k >=100:
            Imagen = 'Seq/Img000'+str(k)+'.jpg'
        if k < 10000 and k >=1000:
            Imagen = 'Seq/Img00'+str(k)+'.jpg'
        # imagenes de carpeta Seq
        inicio = time.time()
        img_read = cv2.imread('Seq/img000325.jpg')  # Imagen de entrada
        #cv2.imshow("imagen real", img_read)
        # Transformamos la imagen de entrada a escala de grises
        gray_img = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)
        # Realizar filtrado bilateral, si cambio los valores del filtro me
        #tiene como parametros de entrada una imagen en 8 bits
        #el 2 parametro representa el rango de diámetro de cada vecindad de píxeles en el proceso de filtrado
        #el 3 parametro representa sigmaColor: el valor sigma del filtro de espacio de color. El valor de este parámetro es grande,
        #lo que indica que los colores más anchos en la vecindad de píxeles se mezclarán, lo que dará como resultado un área de color semi-igual más grande
        #por ultimo el 4 parametro sigmaSpace: el valor sigma del filtro en el espacio de coordenadas. Si el valor es mayor
        #significa que los píxeles más alejados se afectarán entre sí, de modo que un color suficientemente similar en un área más grande obtendrá el mismo color. 
        img_small = cv2.bilateralFilter(gray_img, 15, 50, 50)
        img_big = cv2.bilateralFilter(gray_img, 15, 75, 75)

        # Circulos Pequeños
        small_circles = cv2.HoughCircles(
            img_small,#imagen en un canal 8 bits
            cv2.HOUGH_GRADIENT,#metodo 
            1.2,#Resolucion de pixeles
            3,#Minima distancia entre circulos
            param1=30,#umbral mas alto
            param2=23,#umbral acumulador
            minRadius=8,#minimo radio
            maxRadius=15)#maximo radio

        # Circulos Grandes
        big_circles = cv2.HoughCircles(
            img_big,
            cv2.HOUGH_GRADIENT,
            2.3,
            10,
            param1=100,
            param2=50,
            minRadius=30,
            maxRadius=40)

        counts_small_circles = 0

        # aqui transofrma los datos de las cordenadas y el radio a un int
        if small_circles is not None:
            small_circles = np.around(small_circles).astype("int")
            # Recorrido circulos pequeños
            for i in small_circles[0, :]:
                # Dibuja el borde del círculo
                # parametros(imagen,centro,radio,color,grosor del contorno a dibujar)
                # dibujamos el contorno del circulo encontrado
                cv2.circle(img_read, (i[0], i[1]), i[2], (0, 255, 255), 2)
                counts_small_circles = counts_small_circles + 1  # contador aumenta
                

        counts_big_circles = 0
        count_blue = 0
        count_red = 0
        if big_circles is not None:
            big_circles = np.around(big_circles).astype("int")
            # recorrido circulos grandes
            for i in big_circles[0, :]:
                # Obtener el bgr del centro
                b, g, r = img_read[i[1], i[0]]
                #Para que no tome circulos falsos se agrego un rango de color que no corresponde a los circulos de colores 
                #y un color amarillo por si el centro esta sobre los circulos chicos 
                if b in range(70,180) and g in range(70,180) and r in range(70,180) or b == 0 and g == 255 and r == 255:
                    continue
                elif b > r:
                    # Dibujar el circulo
                    # parametros(imagen,centro,radio,color,grosor del contorno a dibujar)
                    cv2.circle(img_read, (i[0], i[1]), i[2], (0,255,0), 2)
                    # Dibujar el centro
                    cv2.circle(img_read, (i[0], i[1]), 1, (0, 0, 255), 3)
                    count_blue = count_blue + 1
                else:
                    # Dibujar el circulo
                    # parametros(imagen,centro,radio,color,grosor del contorno a dibujar)
                    cv2.circle(img_read, (i[0], i[1]), i[2], (0,255,0), 2)
                    # Dibujar el centro
                    cv2.circle(img_read, (i[0], i[1]), 1, (0, 0, 255), 3)
                    count_red = count_red + 1

                counts_big_circles = counts_big_circles + 1

        fin = time.time()
        delta = fin-inicio
        promedio = promedio + delta
        dividido = dividido + 1
        #print(delta)
    except:
        print ("Error al leer el archivo")


promedix = promedio / dividido
print ("El tiempo de espera total es de :" +str(float(promedio))+ " segundos")
print ("el promedio de ejecucion es de: "+str(float(promedix))+ " segundos")



text_small_circles = "Se encontraron: " + str(counts_small_circles + counts_big_circles) + \
    " Blobs" + ", Small: " + str(counts_small_circles) + ", Big: " + str(counts_big_circles)
text_big_circles = " Blobs Rojo: " + \
    str(count_red) + ", Blobs Azul: " + str(count_blue)
ubication_text_small = (20, 290)
ubication_text_big = (20, 310)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
letter_size = 0.8
color_letter = (0, 0, 0)
letter_thickness = 1
cv2.putText(
    img_read,
    text_small_circles,
    ubication_text_small,
    font,
    letter_size,
    color_letter,
    letter_thickness)
cv2.putText(
    img_read,
    text_big_circles,
    ubication_text_big,
    font,
    letter_size,
    color_letter,
    letter_thickness)

cv2.imshow("Deteccion de Blob y su cantidad", img_read)
cv2.waitKey()
cv2.destroyAllWindows()
