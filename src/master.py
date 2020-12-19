import math, os, time, threading, queue, cv2, socket
import numpy as np
from io import open
from funciones import DatoPWM
from funciones import Discrim
from funciones import Discrim2
from funciones import Discrim3
from funciones import LecturaAzul
from funciones import LecturaRojo
from funciones import LecturaVerde

def ServidorAzul(RobConect,DatoRojo,DatoAzul,DatoVerde,Ja,Jr,Jv)
    sBlue = socket.socket()                   #Abre socket azul
    hostBlue = ''
    portBlue = 3000
    sBlue.bind((hostBlue, portBlue))        
    print("Esperando a Azul")

    sBlue.listen(1)                           #Espera robot azul

    blueClient, addr = sBlue.accept()                  #Genera la conexión con el cliente
    print ('Conectado con: ', addr)
    ConfirmBlue = blueClient.recv(1024)            #Recibe confirmaión de conección
    print(ConfirmBlue)                    #Imprime mensaje de confirmación

    while True:
        ja = Ja.get()

        if ja == 1:
            blueData = DatoAzul.get()
      
            if IniBlue != blueData:
                blueData = str(blueData)
                blueClient.send(blueData.encode())                 #Envía el ciclo de trabajo al cliente
                print('Azul ha cambiado a : ', blueData)
                IniBlue = blueData

def ServidorRojo()
    sRed = socket.socket()                   #Abre socket Rojo
    hostRed = ''
    portRed = 3001
    sRed.bind((hostRed, portRed))        
    print("Esperando a Naranjo")

    sRed.listen(1)                           #Espera robot Rojo

    redClient, addr1 = sRed.accept()  
    print ('Conectado con: ', addr1)
    ConfirmRed = redClient.recv(1024)            #Recibe confirmción de cambio de ciclo de trabajo
    print(ConfirmRed)                    #Imprime mensaje de confirmación
    while True:
        jr = Jr.get()

        if jr == 1:
            redData = DatoRojo.get()
   
            if IniRed != redData:
                redData = str(redData)   
                redClient.send(redData.encode())               #Envía el ciclo de trabajo al cliente
                print('Naranjo ha cambiado a : ', redData)
                IniRed = redData

def SevidorVerde()
    sGreen = socket.socket()                   #Abre socket Rojo
    hostGreen = ''
    portGreen = 3002
    sGreen.bind((hostGreen, portGreen))        
    print("Esperando a Verde")

    sGreen.listen(1)                           #Espera robot Rojo

    greenClient, addr2 = sGreen.accept()  
    print ('Conectado con: ', addr2)
    ConfirmGreen = greenClient.recv(1024)            #Recibe confirmción de cambio de ciclo de trabajo
    print(ConfirmGreen)                    #Imprime mensaje de confirmación

    while True:
        jv = Jv.get(
        if jv == 1:
            greenData = DatoVerde.get()
            if IniGreen != greenData:
                greenData = str(greenData)   
                greenClient.send(greenData.encode())               #Envía el ciclo de trabajo al cliente
                print('Verde ha cambiado a : ', greenData)
                IniGreen = greenData
    

            
                

def LecturaCamara(azx,azy,rox,roy,vex,vey,cex,cey,rosx,rosy,amx,amy,x1,y1,x2,y2,x3,y3,ack):
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

           

           azx.put(xca)
           azy.put(yca)
           vex.put(xca)
           vey.put(yca)
           rox.put(xcr)
           roy.put(ycr)
           rosx.put(xcc)
           rosy.put(ycc)
           amx.put(xcy)
           amy.put(ycy)
           cex.put(xcce)
           cey.put(ycce)
            
           if i == 0:
               azx.get()
               azy.get()
               vex.get()
               vey.get()
               rox.get()
               roy.get()
               rosx.get()
               rosy.get()
               amx.get()
               amy.get()
               cex.get()
               cey.get()
           i=1

           ACK = int(ack.get())
           if ACK == 1:
               X1 = int(x1.get())
               Y1 = int(y1.get())
               X2 = int(x2.get())
               Y2 = int(y2.get())
               X3 = int(x3.get())
               Y3 = int(y3.get())

           if  X1 != 0 and Y1 !=0:
               cv2.circle(imagen,(X1,Y1) ,17,(255,255,255),-1)
           if  X2 != 0 and Y2 !=0:
               cv2.circle(imagen,(X2,Y2) ,17,(255,255,255),-1)
           if  X3 != 0 and Y3 !=0:
               cv2.circle(imagen,(X3,Y3) ,17,(255,255,255),-1)       
           ack.put(0)
           cv2.circle(imagen,(xca,yca) ,1,(255,255,255),-1)
           cv2.circle(imagen,(xcv,ycv) ,1,(255,255,255),-1)
           cv2.circle(imagen,(xcr,ycr) ,1,(255,255,255),-1)
           cv2.circle(imagen,(xcc,ycc) ,1,(255,255,255),-1)
           cv2.circle(imagen,(xcy,ycy) ,1,(255,255,255),-1)
           cv2.circle(imagen,(xcce,ycce) ,1,(255,255,255),-1)


           cv2.line(imagen, (xca,yca), (xcce,ycce), (255,255,255))
           cv2.line(imagen, (xcv,ycv), (xcy,ycy), (255,255,255))
           cv2.line(imagen, (xcr,ycr), (xcc,ycc), (255,255,255))

           cv2.imshow('Camara', imagen)
           
        tecla = cv2.waitKey(5) & 0xFF
        if tecla == 27:
            break
   
    cv2.destroyAllWindows()


def RobAzul(xf,yf,c,ConsMo,azx,azy,cex,cey,DatoAzul,Ja,):
    xr = yr = xo = yo = 0
    ctra=9999
    cmoa=1
    AlpR1=999

    while cmoa == 1:
        xr = azx.get()
        yr = azy.get()
        xo = cex.get()
        yo = cey.get()
        

        while xr == 0 and yr == 0 or xo == 0 and yo == 0 :
            DatoAzul.put(1)
            time.sleep(2)
            xr = azx.get()
            yr = azy.get()
            xo = cex.get()
            yo = cey.get()
        VecAz = ((xf-xr)**2+(yf-yr)**2)**(1/2)
        
        if VecAz >= 12:
            CTRA,DifAz,c,ConsMo,AlpR= DatoPWM(xf,yf,xr,yr,xo,yo,c,ConsMo)
            if AlpR != AlpR1:
                print("Ángulo azul: ",AlpR)
                AlpR1 = AlpR
        else:
            CTRA = 1
            print(CTRA)
            print("UI puede volver a funcionar ")
            PasMovRA = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES
            up = 0
            pit = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/pit.txt","w")
            pit.write(str(up))
            pit.close()
            cmoa = 0

        if CTRA !=ctra:
            #print("Dto ",CTRA)
            #print("Dif ",DifAz)
            #print(ConsMo)
            azul = open("C:/Users/Neftali/Desktop/Comunicación esp/Azul/ordena.txt","w")
            azul.write(str(CTRA))
            azul.close()
            if CTRA == 1:
                time.sleep(1.5)
            ctra = CTRA

    return 

    

def RobRojo(xf,yf,c,ConsMo,rox,roy,rosx,rosy):

    xr = yr = xo = yo = 0
    ctrn=9999
    cmon=1
    AlpR1=1

    while cmon == 1:
    
        xr = rox.get()
        yr = roy.get()
        xo = rosx.get()
        yo = rosy.get()
        
        

        while xr == 0 and yr == 0 or xo == 0 and yo == 0 :
            naranjo = open("C:/Users/Neftali/Desktop/Comunicación esp/Naranjo/ordenn.txt","w")
            naranjo.write(str(1))
            naranjo.close()
            time.sleep(2)
            xr = rox.get()
            yr = roy.get()
            xo = rosx.get()
            yo = rosy.get()
        VecNa = ((xf-xr)**2+(yf-yr)**2)**(1/2)
        if VecNa > 12:
            CTRN,DifNa,c,ConsMo,AlpR = DatoPWM(xf,yf,xr,yr,xo,yo,c,ConsMo)
            if AlpR != AlpR1:
                print("Ángulo rojo: ",AlpR)
                AlpR1=AlpR

        else :
            CTRN = 1
            print(CTRN)
            print("UI puede volver a funcionar ")
            PasMovRN = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES
            up = 0
            pit = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/pit.txt","w")
            pit.write(str(up))
            pit.close()
            cmon = 0
                    

        if CTRN !=ctrn:
            #print("Dto ",CTRN)
            #print("Dif ",DifNa)
            #print(ConsMo)
            naranjo = open("C:/Users/Neftali/Desktop/Comunicación esp/Naranjo/ordenn.txt","w")
            naranjo.write(str(CTRN))
            naranjo.close()
            if CTRN == 1:
                time.sleep(1.5)
            ctrn = CTRN

    return
    

def RobVerde(xf,yf,c,ConsMo,vex,vey,amx,amy):

    xr = yr = xo = yo = 0
    ctrv=9999
    cmov=1
    AlpR1=1
    
    while cmov == 1:
        xr = vex.get()
        yr = vey.get()
        xo = amx.get()
        yo = amy.get()


        while xr == 0 and yr == 0 or xo == 0 and yo == 0 :
            verde = open("C:/Users/Neftali/Desktop/Comunicación esp/Verde/ordenv.txt","w")
            verde.write(str(1))
            verde.close()
            time.sleep(2)
            xr = vex.get()
            yr = vey.get()
            xo = amx.get()
            yo = amy.get()

        VecVe = ((xf-xr)**2+(yf-yr)**2)**(1/2)

        if VecVe > 12:
            CTRV,DifVe,c,ConsMo,AlpR = DatoPWM(xf,yf,xr,yr,xo,yo,c,ConsMo)
            if AlpR > AlpR1+1.5:
                print("Ángulo verde: ",AlpR)
                AlpR1=AlpR
                verde = open("C:/Users/Neftali/Desktop/Comunicación esp/Verde/ordenv.txt","w")
                verde.write(str(1))
                verde.close()
                time.sleep(2)
                
                        
        else :
            CTRV = 1
            print(CTRV)
            print("UI puede volver a funcionar ")
            PasMovRV = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES
            up = 0
            pit = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/pit.txt","w")
            pit.write(str(up))
            pit.close()
            cmov = 0
                    

        if CTRV !=ctrv:
            #print("Dto ",CTRV)
            #print("Dif ",DifVe)
            verde = open("C:/Users/Neftali/Desktop/Comunicación esp/Verde/ordenv.txt","w")
            verde.write(str(CTRV))
            verde.close()
            if CTRV == 1:
                time.sleep(1.5)
            ctrv = CTRV

    return



ax1=ay1=cx1=cy1=vx1=vy1=amx1=amy1=rx1=ry1=rox1=roy1=0
cv = cn = ca = cmov = 0
ConsMoV =ConsMoN = ConsMoA  = 1
ctrv=ctrn=ctra=1000
CTRV=CTRN=CTRA=1
x11=x21=0
la=1
cmon = 1
ja = jr = jv = 0
print("Comienza")

azx = queue.Queue()
azy = queue.Queue()
cex = queue.Queue()
cey = queue.Queue()

rox = queue.Queue()
roy = queue.Queue()
rosx = queue.Queue()
rosy = queue.Queue()

vex = queue.Queue()
vey = queue.Queue()
amx = queue.Queue()
amy = queue.Queue()

x1 = queue.Queue()
yy1 = queue.Queue()
x2 = queue.Queue()
y2 = queue.Queue()
x3 = queue.Queue()
y3 = queue.Queue()
ack = queue.Queue()

RobConect = queue.Queue()
DatoRojo = queue.Queue()
DatoAzul = queue.Queue()
DatoVerde = queue.Queue()
Ja = queue.Queue()
Jv = queue.Queue()
Jr = queue.Queue()

x1.put(0)
yy1.put(0)
x2.put(0)
y2.put(0)
x3.put(0)
y3.put(0)
ack.put(1)

LeerCam = threading.Thread(target=LecturaCamara,args=(azx,azy,rox,roy,vex,vey,cex,cey,rosx,rosy,amx,amy,x1,yy1,x2,y2,x3,y3,ack, ) )
LeerCam.start()

IniServ =  threading.Thread(target=Servidor,args=(RobConect,DatoRojo,DatoAzul,DatoVerde,Ja,Jr,Jv, ) )
IniServ.start()

print("Esperando conección de los robots")
ackser = RobConect.get()
print("Robots Conectados")

while 1:
        
    ax1 = azx.get()
    ay1 = azy.get()
    cx1 = cex.get()
    cy1 = cey.get()

    rx1 = rox.get()
    ry1 = roy.get()
    rox1 = rosx.get()
    roy1 = rosy.get()
        
    vx1 = vex.get()
    y1 = vey.get()
    amx1 = amx.get()
    amy1 = amy.get()

    ### ver si hay movimiento


    print("Para mover de forma automática:1\nPara mover de forma manual: 2\nPara mover 2 robots: 3\nPara mover 3 robots: 4\nPara ordenar robots: 5")
    L1 = input("Ingrese opción>>")
    if L1 == '1':
        print("Insertar coordenadas x,y")
        X1 =input("x >>")
        Y1 = input("y >>")
        RobMov = 0
        X2 = 0
        Y2 = 0
        X3 = 0
        Y3 = 0
        
    
    elif L1 == '2':
        print("Función de momento no disponible")

    elif L1 == '3':
        print("Ha seleccionado mover 2 robot")
        RobMov = 4
        
        print("Insertar coordenadas x,y primer robot")
        X1 =input("x >>")
        Y1 = input("y >>")
        print("Insertar coordenadas x,y segundo robot")
        X2 =input("x >>")
        Y2 = input("y >>")
        X3 = 0
        Y3 = 0

    elif L1 == '4':
        print("Se moverán los 3 robots")
        RobMov = 5
        
        print("Insertar coordenadas x,y primer robot")
        X1 =input("x >>")
        Y1 = input("y >>")
        print("Insertar coordenadas x,y segundo robot")
        X2 =input("x >>")
        Y2 = input("y >>")
        print("Insertar coordenadas x,y tercer robot robot")
        X3 =input("x >>")
        Y3 = input("y >>")
        
    elif L1 == '5':
        print("Se moverán los 3 robots")
        RobMov = 5        
        print("Línea vertical: 1\n Línea Horizontal: 2\n Triangulo: 3")
        TipLin = input("Opción >>")
        if TipLin == '1':
            X1 = 628
            Y1 = 200
            X2 = 628
            Y2 = 400
            X3 = 628
            Y3 = 600
        elif TipLin == '2':
            X1 = 200
            Y1 = 400
            X2 = 620
            Y2 = 400
            X3 = 1040
            Y3 = 400
        elif TipLin == '3' :
            X1 = 628
            Y1 = 150
            X2 = 845
            Y2 = 525
            X3 = 411
            Y3 = 525
            
        else:
            print("Opción no válida")


        
    else :
        print("Opción ingresada no válida")

        
    x1.put(X1)
    yy1.put(Y1)
    x2.put(X2)
    y2.put(Y2)
    x3.put(X3)
    y3.put(Y3)
    ack.put(1)

    if RobMov == 0: #Solo uno de forma automática
        xfra,yfra,xfrr,yfrr,xfrv,yfrv = Discrim(X1,Y1,ax1,ay1,rx1,ry1,vx1,vy1)
        VecAz = ((xfra-ax1)**2+(yfra-ay1)**2)**(1/2) #Distancia entre puntos
        VecNa = ((xfrr-rx1)**2+(yfrr-ry1)**2)**(1/2)
        VecVe = ((xfrv-vx1)**2+(yfrv-vy1)**2)**(1/2)
    elif RobMov == 4: #Solo dos de forma automática
        xfra,yfra,xfrr,yfrr,xfrv,yfrv = Discrim2(X1,Y1,X2,Y2,ax1,ay1,rx1,ry1,vx1,vy1)
        VecAz = ((xfra-ax1)**2+(yfra-ay1)**2)**(1/2) #Distancia entre puntos
        VecNa = ((xfrr-rx1)**2+(yfrr-ry1)**2)**(1/2)
        VecVe = ((xfrv-vx1)**2+(yfrv-vy1)**2)**(1/2)
    elif RobMov == 5:
        xfra,yfra,xfrr,yfrr,xfrv,yfrv = Discrim3(X1,Y1,X2,Y2,X3,Y3,ax1,ay1,rx1,ry1,vx1,vy1)
        VecAz = ((xfra-ax1)**2+(yfra-ay1)**2)**(1/2) #Distancia entre puntos
        VecNa = ((xfrr-rx1)**2+(yfrr-ry1)**2)**(1/2)
        VecVe = ((xfrv-vx1)**2+(yfrv-vy1)**2)**(1/2)
            
    if la == 1:
        print("Vector azul: ",VecAz)
        print("Vector Rojo: ",VecNa)
        print("Vector Verde: ",VecVe)
        la =0

    if VecAz >= 12:
        MovRoAz = threading.Thread(target=RobAzul, args=(xfra,yfra,ca,ConsMoA,azx,azy,cex,cey,DatoAzul,Ja, ))
        MovRoAz.start()
        Ja.put(1)
        ja=1
    else:
        Ja.put(0)
                
    if VecNa >= 12:
        MovRoRo = threading.Thread(target=RobRojo, args=(xfrr,yfrr,cn,ConsMoN,rox,roy,rosx,rosy, ))
        MovRoRo.start()
        Jr.put(1)
        jr = 1
    else:
        Jr.put(0)

    if VecVe >= 12:
        MovRoVe = threading.Thread(target=RobVerde, args=(xfrv,yfrv,cv,ConsMoV,vex,vey,amx,amy, ))
        MovRoVe.start()
        Jv.put(1)
        jv = 1
    else:
        Jv.put(1)

    if ja == 1:
        MovRoAz.join()

    if jr == 1:
        MovRoRo.join()

    if jv == 1:
        MovRoVe.join()

    ja = 0
    jr = 0
    jv = 0
    pi = 0    


        
            
            
            

