import math, os, time, threading, cv2
import numpy as np
from io import open
from funciones import DatoPWM
from funciones import Discrim
from funciones import Discrim2
from funciones import Discrim3
from funciones import LecturaAzul
from funciones import LecturaRojo
from funciones import LecturaVerde
from collections import deque


def LecturaCamara(azx,azy,rox,roy,vex,vey,cex,cey,rosx,rosy,amx,amy):
    captura = cv2.VideoCapture(0)
    RobMov =0

    
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
           bajosC = np.array([107,47,101], dtype=np.uint8)
           altosC = np.array([208,86,142], dtype=np.uint8) 

       #Guardamos el rango de colores hsv (amarillo)
           bajosY = np.array([23,232,119], dtype=np.uint8)
           altosY = np.array([40,255,189], dtype=np.uint8)

       #Guardamos el rango de colores hsv (celeste)
           bajosCE = np.array([89,130,154], dtype=np.uint8)
           altosCE = np.array([110,225,175], dtype=np.uint8)
       
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

           azx.append(xca)
           azy.append(yca)
           vex.append(xca)
           vey.append(yca)
           rox.append(xcr)
           roy.append(ycr)
           rosx.append(xcc)
           rosy.append(ycc)
           amx.append(xcy)
           amy.append(ycy)
           cex.append(xcce)
           cey.append(ycce)
            
           if i == 0:
               azx.popleft(xca)
               azy.popleft(yca)
               vex.popleft(xca)
               vey.popleft(yca)
               rox.popleft(xcr)
               roy.popleft(ycr)
               rosx.popleft(xcc)
               rosy.popleft(ycc)
               amx.popleft(xcy)
               amy.popleft(ycy)
               cex.popleft(xcce)
               cey.popleft(ycce)
           i=1
               
        
           cv2.circle(imagen,(xca,yca) ,1,(255,255,255),-1)
       #print("xca=",xca,"yca=",yca)
           #cv2.imshow('maskA', maskA)

           cv2.circle(imagen,(xcv,ycv) ,1,(255,255,255),-1)
       #print("xcv=",xcv,"ycv=",ycv)
           #cv2.imshow('maskV', maskV)

           cv2.circle(imagen,(xcr,ycr) ,1,(255,255,255),-1)
       #print("xcr=",xcr,"ycr=",ycr)
           #cv2.imshow('maskR', maskR)

           cv2.circle(imagen,(xcc,ycc) ,1,(255,255,255),-1)
       #print("xcc=",xcc,"ycc=",ycc)
           #cv2.imshow('maskC', maskC)

           cv2.circle(imagen,(xcy,ycy) ,1,(255,255,255),-1)
       #print("xcy=",xcy,"ycy=",ycy)

           cv2.circle(imagen,(xcce,ycce) ,1,(255,255,255),-1)
       #print("xcce=",xcce,"ycce=",ycce)
           #cv2.imshow('maskCE', maskCE)

           cv2.imshow('Camara', imagen)


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
thread1 = threading.Thread(target=LecturaCamara,args=(azx,azy,rox,roy,vex,vey,cex,cey,rosx,rosy,amx,amy, ) )
thread1.start()
while(1):
    "ax=int(azx)"
    print(azx)

