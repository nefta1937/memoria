#Librerias
import cv2
import numpy as np
from collections import deque
from statistics import mean
   
#Iniciar camara
captura = cv2.VideoCapture(0)
RobMov =0

azx = deque()
rox = deque()
vex = deque()
cex = deque()
rosx = deque()
amx = deque()
azy = deque()
roy = deque()
vey = deque()
cey = deque()
rosy = deque()
amy = deque()
i=0

while(1):
   
    #Caputrar una imagen y convertirla a hsv
    valido, imagen1 = captura.read()
    imagen = imagen1[10:800, 25:1230]
    if valido:
       hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
       
       #Guardamos el rango de colores hsv (azules)
       bajosA = np.array([113,181,89], dtype=np.uint8)
       altosA = np.array([196,255,169], dtype=np.uint8) 

       #Guardamos el rango de colores hsv (verde)
       bajosV = np.array([52,147,51], dtype=np.uint8)
       altosV = np.array([68,231,211], dtype=np.uint8)

       #Guardamos el rango de colores hsv (rojo)
       bajosR = np.array([0,178,98], dtype=np.uint8)
       altosR = np.array([21,222,211], dtype=np.uint8)

       #Guardamos el rango de colores hsv (rosado)
       bajosC = np.array([116,56,130], dtype=np.uint8)
       altosC = np.array([136,92,169], dtype=np.uint8) 

       #Guardamos el rango de colores hsv (amarillo)
       bajosY = np.array([23,232,119], dtype=np.uint8)
       altosY = np.array([40,255,189], dtype=np.uint8)

       #Guardamos el rango de colores hsv (celeste)
       bajosCE = np.array([80,160,139], dtype=np.uint8)
       altosCE = np.array([112,231,228], dtype=np.uint8)
       
       #Crear una mascara que detecte los colores
       maskA = cv2.inRange(hsv, bajosA, altosA)
       maskV = cv2.inRange(hsv, bajosV, altosV)
       maskR = cv2.inRange(hsv, bajosR, altosR)
       maskC = cv2.inRange(hsv, bajosC, altosC)
       maskY = cv2.inRange(hsv, bajosY, altosY)
       maskCE = cv2.inRange(hsv, bajosCE, altosCE)
       
       #Filtrar el ruido con un CLOSE seguido de un OPEN
       kernel = np.ones((0,0),np.uint8)
       kernelros = np.ones((20,20),np.uint8)
       
       maskA = cv2.morphologyEx(maskA, cv2.MORPH_CLOSE, kernel)
       maskA = cv2.morphologyEx(maskA, cv2.MORPH_OPEN, kernel)

       maskV = cv2.morphologyEx(maskV, cv2.MORPH_CLOSE, kernel)
       maskV = cv2.morphologyEx(maskV, cv2.MORPH_OPEN, kernel)

       maskR = cv2.morphologyEx(maskR, cv2.MORPH_CLOSE, kernelros)
       maskR = cv2.morphologyEx(maskR, cv2.MORPH_OPEN, kernelros)

       maskC = cv2.morphologyEx(maskC, cv2.MORPH_CLOSE, kernel)
       maskC = cv2.morphologyEx(maskC, cv2.MORPH_OPEN, kernel)

       maskY = cv2.morphologyEx(maskY, cv2.MORPH_CLOSE, kernel)
       maskY = cv2.morphologyEx(maskY, cv2.MORPH_OPEN, kernel)

       maskCE = cv2.morphologyEx(maskCE, cv2.MORPH_CLOSE, kernel)
       maskCE = cv2.morphologyEx(maskCE, cv2.MORPH_OPEN, kernel)

       #Crear cuadrado
       xa,ya,wa,ha = cv2.boundingRect(maskA)
       xv,yv,wv,hv = cv2.boundingRect(maskV)
       xr,yr,wr,hr = cv2.boundingRect(maskR)
       xc,yc,wc,hc = cv2.boundingRect(maskC)
       xy,yy,wy,hy = cv2.boundingRect(maskY)
       xce,yce,wce,hce = cv2.boundingRect(maskCE)
       
       #Difuminamos la mascara para suavizar los contornos y aplicamos filtro canny
       blur = cv2.GaussianBlur(maskA, (5, 5), 0)
       edges = cv2.Canny(maskA,1,2)

       blur = cv2.GaussianBlur(maskV, (5, 5), 0)
       edges = cv2.Canny(maskV,1,2)

       blur = cv2.GaussianBlur(maskR, (5, 5), 0)
       edges = cv2.Canny(maskR,1,2)

       #Crea punto al centro de cada figura de color
       xca = xa+wa//2
       yca = ya+ha//2
         
       xcv = xv+wv//2
       ycv = yv+hv//2
       
       xcr = xr+wr//2
       ycr = yr+hr//2
       
       xcc = xc+wc//2
       ycc = yc+hc//2    

       xcy = xy+wy//2
       ycy = yy+hy//2
       
       xcce = xce+wce//2
       ycce = yce+hce//2     
       '''if i<10:
           if xca != 0 and yca != 0:
               azx.append(xca)
               azy.append(yca)
           if xcr != 0 and ycr != 0:
               rox.append(xcr)
               roy.append(ycr)
           if xcv != 0 and ycv != 0:
               vex.append(xcv)
               vey.append(ycv)
           if xcce != 0 and ycce != 0: 
               cex.append(xcce)
               cey.append(ycce)
           if xcc != 0 and ycc != 0: 
               rosx.append(xcc)
               rosy.append(ycc)
           if xcy != 0 and ycy != 0: 
               amx.append(xcy)
               amy.append(ycy)
           i = i+1
       else:
           if xca != 0 and yca != 0:
               azx.append(xca)
               azy.append(yca)
               azx.popleft()
               azy.popleft()
           if xcr != 0 and ycr != 0:
               rox.append(xcr)
               roy.append(ycr)
               rox.popleft()
               roy.popleft()
           if xcv != 0 and ycv != 0:           
               vex.append(xcv)
               vey.append(ycv)
               vex.popleft()
               vey.popleft()
           if xcce != 0 and ycce != 0: 
               cex.append(xcce)
               cey.append(ycce)
               cex.popleft()
               cey.popleft()
           if xcc != 0 and ycc != 0: 
               rosx.append(xcc)
               rosy.append(ycc)
               rosx.popleft()
               rosy.popleft()
           if xcy != 0 and ycy != 0: 
               amx.append(xcy)
               amy.append(ycy)
               amx.popleft()
               amy.popleft()

       if xca == 0 and yca == 0:
           xca = int(mean(azx))
           yca = int(mean(azy))
       if xcr == 0 and ycr == 0:
           xcr = int(mean(rox))
           ycr = int(mean(roy)) 
       if xcr == 0 and ycr == 0:
           xcv = int(mean(vex))
           ycv = int(mean(vey))
       if xcce == 0 and ycce == 0:
           xcce = int(mean(cex))
           ycce = int(mean(cey)) 
       if xcc == 0 and ycc == 0:
           xcc = int(mean(rosx))
           ycc = int(mean(rosy))
       if xcy == 0 and ycy == 0:
           xcy = int(mean(amx))
           ycy = int(mean(amy))'''
        
        
       cv2.circle(imagen,(xca,yca) ,1,(255,255,255),-1)
       #print("xca=",xca,"yca=",yca)
       cv2.imshow('maskA', maskA)

       cv2.circle(imagen,(xcv,ycv) ,1,(255,255,255),-1)
       #print("xcv=",xcv,"ycv=",ycv)
       cv2.imshow('maskV', maskV)

       cv2.circle(imagen,(xcr,ycr) ,1,(255,255,255),-1)
       #print("xcr=",xcr,"ycr=",ycr)
       cv2.imshow('maskR', maskR)

       cv2.circle(imagen,(xcc,ycc) ,1,(255,255,255),-1)
       #print("xcc=",xcc,"ycc=",ycc)
       cv2.imshow('maskC', maskC)

       cv2.circle(imagen,(xcy,ycy) ,1,(255,255,255),-1)
       #print("xcy=",xcy,"ycy=",ycy)

       cv2.circle(imagen,(xcce,ycce) ,1,(255,255,255),-1)
       #print("xcce=",xcce,"ycce=",ycce)
       cv2.imshow('maskCE', maskCE)
       
       X1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X1.txt","r")
       x1 = int(X1.read())
       X1.close()
       Y1 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y1.txt","r")
       y1 = int(Y1.read())
       Y1.close()

       X2 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X2.txt","r")
       x2 = int(X2.read())
       X2.close()
       Y2 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y2.txt","r")
       y2 = int(Y2.read())
       Y2.close()

       X3 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/X3.txt","r")
       x3 = int(X3.read())
       X3.close()
       Y3 = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Y3.txt","r")
       y3 = int(Y3.read())
       Y3.close()

       robMov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/RobMov.txt","r")
       Robmov = int(robMov.read())
       robMov.close()

       per = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/per.txt","w")
       per.write(str(0))
       per.close()

       cv2.circle(imagen,(x1,y1),17,(255,255,255),-1)
       #cv2.circle(imagen,(x2,y2),17,(255,255,255),-1)
       #cv2.circle(imagen,(x3,y3),17,(255,255,255),-1)

       if Robmov == 4:
           cv2.circle(imagen,(x2,y2),17,(255,255,255),-1)

       if Robmov == 5:
           cv2.circle(imagen,(x2,y2),17,(255,255,255),-1)
           cv2.circle(imagen,(x3,y3),17,(255,255,255),-1)

           
           
       
       azulx = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/azul/x.txt","w")
       azuly = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/azul/y.txt","w")
       azulx.write(str(xca))
       azuly.write(str(yca))
       azulx.close()
       azuly.close()

       verdex = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/verde/x.txt","w")
       verdey = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/verde/y.txt","w")
       verdex.write(str(xcv))
       verdey.write(str(ycv))
       verdex.close()
       verdey.close()

       rojox = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/rojo/x.txt","w")
       rojoy = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/rojo/y.txt","w")
       rojox.write(str(xcr))
       rojoy.write(str(ycr))
       rojox.close()
       rojoy.close()

       rosadox = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/cafe/x.txt","w")
       rosadoy = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/cafe/y.txt","w")
       rosadox.write(str(xcc))
       rosadoy.write(str(ycc))
       rosadox.close()
       rosadoy.close()

       amarillox = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/amarillo/x.txt","w")
       amarilloy = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/amarillo/y.txt","w")
       amarillox.write(str(xcy))
       amarilloy.write(str(ycy))
       amarillox.close()
       amarilloy.close()

       
       celestex = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/celeste/x.txt","w")
       celestey = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/celeste/y.txt","w")
       celestex.write(str(xcce))
       celestey.write(str(ycce))
       celestex.close()
       celestey.close()

       per = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/per.txt","w")
       per.write(str(1))
       per.close()

       cv2.line(imagen, (xca,yca), (xcce,ycce), (255,255,255))
       cv2.line(imagen, (xcv,ycv), (xcy,ycy), (255,255,255))
       cv2.line(imagen, (xcr,ycr), (xcc,ycc), (255,255,255))


       
       cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
   
cv2.destroyAllWindows()
