import math
import os
from io import open
import time
import threading
from Funciones import DatoPWM
from Funciones import Discrim
from Funciones import Discrim2
from Funciones import Discrim3
from Camara import CameraVisor

def GetRobotFileName(robotName):
    if robotName === 'Azul':
        return "C:/Users/Neftali/Desktop/Comunicación esp/Azul/ordena.txt"

def RobAzul(xf,yf,xr,yr,xo,yo,c,ConsMo,ctra):
    if VecAz >= 12:
        CTRA,DifAz,c,ConsMo= DatoPWM(xf,yf,xr,yr,xo,yo,c,ConsMo)
                    
    else:
        CTRA = 1
        print(CTRA)
        print("UI puede volver a funcionar ")
        PasMovRA = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES
        up = 0
        pit = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/pit.txt","w")
        pit.write(str(up))
        pit.close()
        cmon = 0

    if CTRA !=ctra:
        print("Dto ",CTRA)
        print("Dif ",DifAz)
        print(ConsMo)
        azul = open("C:/Users/Neftali/Desktop/Comunicación esp/Azul/ordena.txt","w")
        azul.write(str(CTRA))
        azul.close()
        if CTRA == 1:
            time.sleep(1.2)
        ctra = CTRA

def RobVerde(xf,yf,xr,yr,xo,yo,c,ConsMo,ctrn):
    if VecNa > 12:
        CTRN,DifNa,c,ConsMo = DatoPWM(xf,yf,xr,yr,xo,yo,c,ConsMo)

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
        print("Dto ",CTRN)
        print("Dif ",DifNa)
        print(ConsMo)
        naranjo = open("C:/Users/Neftali/Desktop/Comunicación esp/Naranjo/ordenn.txt","w")
        naranjo.write(str(CTRN))
        naranjo.close()
        if CTRN == 1:
            time.sleep(1.2)
        ctrn = CTRN
    

def RobRojo(xf,yf,xr,yr,xo,yo,c,ConsMo,ctrv):
    if VecVe > 12:
        CTRV,DifVe,cv,ConsMo = DatoPWM(xf,yf,xr,yr,xo,yo,c,ConsMo)
                        
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
        print("Dto ",CTRV)
        print("Dif ",DifVe)
        print(ConsMo)
        verde = open("C:/Users/Neftali/Desktop/Comunicación esp/Verde/ordenv.txt","w")
        verde.write(str(CTRV))
        verde.close()
        if CTRV == 1:
            time.sleep(1.2)
        ctrv = CTRV

ax1=ay1=cx1=cy1=vx1=vy1=amx1=amy1=rx1=ry1=rox1=roy1=0
cv = cn = ca = cmov = 0
ConsMoV =ConsMoN = ConsMoA  = 1
ctrv=ctrn=ctra=1000
CTRV=CTRN=CTRA=1
x11=x21=0
la=1
cmon = 1

visor = new VisorCamera()
thread.stavisor.initProcess()

while(1):
    per = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/per.txt","r")
    p = per.read()
    per.close()

    pitr = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/pit.txt","r")
    pi = pitr.read()
    pitr.close()

    if p == '1' and pi == '1' :
        azulx = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/azul/x.txt","r")
        azuly = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/azul/y.txt","r")
        ax = azulx.read() 
        ay = azuly.read()
        azulx.close()
        azuly.close()
         
        celestex = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/celeste/x.txt","r")
        celestey = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/celeste/y.txt","r")
        cx = celestex.read()
        cy = celestey.read()
        celestex.close()
        celestey.close()

        verdex = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/verde/x.txt","r")
        verdey = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/verde/y.txt","r")
        vx = verdex.read()
        vy = verdey.read()
        verdex.close()
        verdey.close()        
    
        amarillox = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/amarillo/x.txt","r")
        amarilloy = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/amarillo/y.txt","r")
        amx = amarillox.read()
        amy = amarilloy.read()
        amarillox.close()
        amarilloy.close()
        
        rojox = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/rojo/x.txt","r")
        rojoy = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/rojo/y.txt","r")
        rx = rojox.read()
        ry = rojoy.read()
        rojox.close()
        rojoy.close()
    
        rosadox = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/cafe/x.txt","r")
        rosadoy = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/cafe/y.txt","r")
        rox = rosadox.read() 
        roy = rosadoy.read()
        rosadox.close()
        rosadoy.close()
        
        if ax is None:
            ax = ax1
        if ay is None:
            ay = ay1
        ax1 = int(ax)
        ay1 = int(ay)

        if cx is None:
            cx = cx1
        if cy is None:
            cy = cy1
        cx1 = int(cx)
        cy1 = int(cy)

        if amx is None:
            amx = am1
        if ay is None:
            amy = am1
        amx1 = int(amx)
        amy1 = int(amy)

        if vx is None:
            vx = vx1
        if ay is None:
            vy = vy1
        vx1 = int(vx)
        vy1 = int(vy)

        if rx is None:
            rx = rx1
        if ry is None:
            ry = ry1
        rx1 = int(rx)
        ry1 = int(ry)

        if rox is None:
            rox = rox1
        if roy is None:
            roy = roy1S
        rox1 = int(rox)
        roy1 = int(roy)

    ### ver si hay movimiento

        robMov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/RobMov.txt","r")
        Robmov = robMov.read()
        robMov.close()

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

        if RobMov == '0': #Solo uno de forma automática
            xfra,yfra,xfrr,yfrr,xfrv,yfrv = Discrim2(x1,y1,x2,y2,ax1,ay1,rx1,ry1,vx1,vy1)
            VecAz = ((xfra-ax1)**2+(yfra-ay1)**2)**(1/2) #Distancia entre puntos
            VecNa = ((xfrr-rx1)**2+(yfrr-ry1)**2)**(1/2)
            VecVe = ((xfrv-vx1)**2+(yfrv-vy1)**2)**(1/2)
        elif RobMov == '4': #Solo dos de forma automática
            xfra,yfra,xfrr,yfrr,xfrv,yfrv = Discrim2(x1,y1,x2,y2,ax1,ay1,rx1,ry1,vx1,vy1)
            VecAz = ((xfra-ax1)**2+(yfra-ay1)**2)**(1/2) #Distancia entre puntos
            VecNa = ((xfrr-rx1)**2+(yfrr-ry1)**2)**(1/2)
            VecVe = ((xfrv-vx1)**2+(yfrv-vy1)**2)**(1/2)
        elif RobMov == '5':
            xfra,yfra,xfrr,yfrr,xfrv,yfrv = Discrim3(x1,y1,x2,y2,x3,y3,ax1,ay1,rx1,ry1,vx1,vy1)

            VecAz = ((xfra-ax1)**2+(yfra-ay1)**2)**(1/2) #Distancia entre puntos
            VecNa = ((xfrr-rx1)**2+(yfrr-ry1)**2)**(1/2)
            VecVe = ((xfrv-vx1)**2+(yfrv-vy1)**2)**(1/2)
            
        if la == 1:
            print("Vector azul: ",VecAz)
            print("Vector Rojo: ",VecNa)
            print("Vector Verde: ",VecVe)
            la =0

        if VecAz >= 12:
            if cea == 1:
                cea = 0
                MovRoAz = threading.Thread(target=RobAzul, args=(xfra,yfra,ax1,ay1,cx1,cy1,ca,ConsMoA,))
                MovRoAz.start()
                ##Mover robot Azul
                #Abrir hilo de robot azul
        else:
            cba = 1
            #Da paso a bloquear robot

        if VecNa >= 12:
            if cen == 1:
                cea = 0
                MovRoNa = threading.Thread(target=RobRojo, args=(xfrv,yfrv,vx1,vy1,amx1,amy1,cv,ConsMoV,))
                MovRoNa.start()
                ##Mover robot Azul
                #Abrir hilo de robot azul

        else:
            cbn = 1
            #Da paso a bloquear robot

        if VecVe >= 12:
            if cev == 1:
                cev = 0
                MovRoVe = threading.Thread(target=RobAzul, args=(x1,y1,ax1,ay1,cx1,cy1,ca,ConsMoA,))
                MovRoVe.start()
                ##Mover robot Azul
                #Abrir hilo de robot azul

        else:
            cbv = 1
            #Da paso a bloquear robot


        if cba == 1 and cbn == 1 and cbv == 1 : ##aqui se detiene todo
            ## bloquear todo movimiento hasta nuevo aviso
            
        
            
            
            
