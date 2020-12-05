import math, os, time, threading 
from io import open
from Funciones import DatoPWM
from Funciones import Discrim
from Funciones import Discrim2
from Funciones import Discrim3
from Funciones import LecturaAzul
from Funciones import LecturaRojo
from Funciones import LecturaVerde

def RobAzul(xf,yf,c,ConsMo):
    xr = yr = xo = yo = 0
    ctra=9999
    cmoa=1
    AlpR1=999

    while cmoa == 1:
        xr,yr,xo,yo = LecturaAzul(xr,yr,xo,yo)
        VecAz = ((xf-xr)**2+(yf-yr)**2)**(1/2)

        while xr == 0 and yr == 0 or xo == 0 and yo == 0 :
            azul = open("C:/Users/Neftali/Desktop/Comunicación esp/Azul/ordena.txt","w")
            azul.write(str(1))
            azul.close()
            time.sleep(2)
            xr,yr,xo,yo = LecturaAzul(xr,yr,xo,yo)

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

    

def RobRojo(xf,yf,c,ConsMo):

    xr = yr = xo = yo = 0
    ctrn=9999
    cmon=1
    AlpR1=1

    while cmon == 1:
    
        xr,yr,xo,yo = LecturaRojo(xr,yr,xo,yo)
        VecNa = ((xf-xr)**2+(yf-yr)**2)**(1/2)

        while xr == 0 and yr == 0 or xo == 0 and yo == 0 :
            naranjo = open("C:/Users/Neftali/Desktop/Comunicación esp/Naranjo/ordenn.txt","w")
            naranjo.write(str(1))
            naranjo.close()
            time.sleep(2)
            xr,yr,xo,yo = LecturaRojo(xr,yr,xo,yo)
    
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
    

def RobVerde(xf,yf,c,ConsMo):

    xr = yr = xo = yo = 0
    ctrv=9999
    cmov=1
    AlpR1=1
    
    while cmov == 1:
        xr,yr,xo,yo = LecturaVerde(xr,yr,xo,yo)
        VecVe = ((xf-xr)**2+(yf-yr)**2)**(1/2)

        while xr == 0 and yr == 0 or xo == 0 and yo == 0 :
            verde = open("C:/Users/Neftali/Desktop/Comunicación esp/Verde/ordenv.txt","w")
            verde.write(str(1))
            verde.close()
            time.sleep(2)
            xr,yr,xo,yo = LecturaVerde(xr,yr,xo,yo)

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

while 1:
    per = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/per.txt","r")
    p = per.read()
    per.close()

    pit = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/pit.txt","r")
    pi = pit.read()
    pit .close()

    if p == '1' and pi == '1' :        
        ax1,ay1,cx1,cy1 = LecturaAzul(ax1,ay1,cx1,cy1)
        rx1,ry1,rox1,roy1 = LecturaRojo(rx1,ry1,rox1,roy1)
        vx1,vy1,amx1,amy1 = LecturaVerde(vx1,vy1,amx1,amy1)
        print("Leyó")
    ### ver si hay movimiento

        robMov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/RobMov.txt","r")
        RobMov = robMov.read()
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
            xfra,yfra,xfrr,yfrr,xfrv,yfrv = Discrim(x1,y1,ax1,ay1,rx1,ry1,vx1,vy1)
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
            print("entró al robot")
            MovRoAz = threading.Thread(target=RobAzul, args=(xfra,yfra,ca,ConsMoA, ))
            MovRoAz.start()
            ja=1
            
                ##Mover robot Azul
                #Abrir hilo de robot azul
                
        if VecNa >= 12:
            MovRoRo = threading.Thread(target=RobRojo, args=(xfrr,yfrr,cn,ConsMoN, ))
            MovRoRo.start()
            jr = 1
                ##Mover robot Azul
                #Abrir hilo de robot azul


        if VecVe >= 12:
            MovRoVe = threading.Thread(target=RobVerde, args=(xfrv,yfrv,cv,ConsMoV, ))
            MovRoVe.start()
            jv = 1
                ##Mover robot Azul
                #Abrir hilo de robot azul

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


        
            
            
            

