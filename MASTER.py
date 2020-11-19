import math
import os
from io import open
import time
from Funciones import DatoPWM
from Funciones import Discrim2
from Funciones import Discrim3

ax1=ay1=cx1=cy1=vx1=vy1=amx1=amy1=rx1=ry1=rox1=roy1=0
cv = cn = ca = cmov = 0
ConsMoV =ConsMoN = ConsMoA  = 1
ctrv=ctrn=ctra=1000
CTRV=CTRN=CTRA=1
x11=x21=0
la=1
cmon = 1
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
            roy = roy1
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

        if Robmov == '0': ##automático
            VecAz = ((x1-ax1)**2+(y1-ay1)**2)**(1/2) #Distancia entre puntos
            VecNa = ((x1-rx1)**2+(y1-ry1)**2)**(1/2)
            VecVe = ((x1-vx1)**2+(y1-vy1)**2)**(1/2)
            if cmov == 0:
                cmov = 1
                print("La Distancia del robot azul al punto es: ",VecAz,"\nLa Distancia del robot naranjo al punto es: ",VecNa,"\nLa Distancia del robot verde al punto es: ",VecVe)
            ############################################################
            if VecAz <= VecNa and VecAz <=VecVe and VecAz <= VecVe:
                if VecAz >= 12:
                    CTRA,DifAz,ca,ConsMoA = DatoPWM(x1,y1,ax1,ay1,cx1,cy1,ca,ConsMoA)
                    
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
                    print(ConsMoA)
                    azul = open("C:/Users/Neftali/Desktop/Comunicación esp/Azul/ordena.txt","w")
                    azul.write(str(CTRA))
                    azul.close()
                    if CTRA == 1:
                        time.sleep(1.2)
                    ctra = CTRA
                
            ###########################################################        
            elif VecNa <= VecVe and VecNa <=VecAz:

                if VecNa > 12:
                    CTRN,DifNa,cn,ConsMoN = DatoPWM(x1,y1,rx1,ry1,rox1,roy1,cn,ConsMoN)

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
                    print(ConsMoN)
                    naranjo = open("C:/Users/Neftali/Desktop/Comunicación esp/Naranjo/ordenn.txt","w")
                    naranjo.write(str(CTRN))
                    naranjo.close()
                    if CTRN == 1:
                        time.sleep(1)
                    ctrn = CTRN
            #####################################################   
            else:
                
                if VecVe > 12:
                    CTRV,DifVe,cv,ConsMoV = DatoPWM(x1,y1,vx1,vy1,amx1,amy1,cv,ConsMoV)
                        
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
                    print(ConsMoV)
                    verde = open("C:/Users/Neftali/Desktop/Comunicación esp/Verde/ordenv.txt","w")
                    verde.write(str(CTRV))
                    verde.close()
                    if CTRV == 1:
                        time.sleep(1)
                    ctrv = CTRV

        ##########################################################        
        elif Robmov == '1':##mover azul
            H=0

        elif Robmov == '2':##mover naranjo
            H=0

        elif Robmov == '3':##mover verde
            H=0

        elif Robmov == '4':##mover dos
            xfra,yfra,xfrr,yfrr,xfrv,yfrv = Discrim2(x1,y1,x2,y2,ax1,ay1,rx1,ry1,vx1,vy1)

            VecAz = ((xfra-ax1)**2+(yfra-ay1)**2)**(1/2) #Distancia entre puntos
            VecNa = ((xfrr-rx1)**2+(yfrr-ry1)**2)**(1/2)
            VecVe = ((xfrv-vx1)**2+(yfrv-vy1)**2)**(1/2)

            if la == 1:
                print("Vector azul: ",VecAz)
                print("Vector Rojo: ",VecNa)
                print("Vector Verde: ",VecVe)
                la =0
            if x11 != x1 and x21 != x2:
                c11 = 1
                c12 = 1
                c13 = 1

            if VecAz >= 12:
                CTRA,DifAz,ca,ConsMoA = DatoPWM(x1,y1,ax1,ay1,cx1,cy1,ca,ConsMoA)
                print("CTRA: ",CTRA)
                if c11 == 1:
                    if xfra == x1:
                        print("Robot azul a punto 1")
                    elif xfra == x2:
                        print("Robot azul a punto 2")
                    else:
                        print("Robot azul no se mueve")
                    c11 = 0
                    
            else:
                    print("No vuelve a entrar a azul")
                    CTRA = 1
                    PasMovRA = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES
                    cmon = 0

            if CTRA !=ctra:
                print("Dto azul ",CTRA)
                azul = open("C:/Users/Neftali/Desktop/Comunicación esp/Azul/ordena.txt","w")
                azul.write(str(CTRA))
                azul.close()
                if CTRA == 1:
                    time.sleep(.5)
                ctra = CTRA
                    

                
            if VecNa >= 12 :
                CTRN,DifNa,cn,ConsMoN = DatoPWM(x1,y1,ax1,ay1,cx1,cy1,cn,ConsMoN)
                print("CTRN: ",CTRN)
                if c12 == 1:
                    if xfrr == x1:
                        print("Robot rojo a punto 1")
                    elif xfrr == x2:
                        print("Robot rojo a punto 2")
                    else:
                        print("Robot rojo no se mueve")
                    c12 = 0

            else :
                    CTRN = 1
                    PasMovRN = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES
                    cmon = 0
                    

            if CTRN !=ctrn:
                print("Dto rojo ",CTRN)
                naranjo = open("C:/Users/Neftali/Desktop/Comunicación esp/Naranjo/ordenn.txt","w")
                naranjo.write(str(CTRN))
                naranjo.close()
                if CTRN == 1:
                    time.sleep(.5)
                ctrn = CTRN



            if VecVe >= 12 :
                CTRV,DifVe,cv,ConsMoV = DatoPWM(x1,y1,ax1,ay1,cx1,cy1,ca,ConsMoV)
                print("CTRV: ",CTRV)
                if c13 == 1:
                    if xfrv == x1:
                        print("Robot verde a punto 1")
                    elif xfrv == x2:
                        print("Robot verde a punto 2")
                    else:
                        print("Robot verde no se mueve")
                    c13 = 0

            else :
                    CTRV = 1
                    print(CTRV)
                    #print("UI puede volver a funcionar ")
                    PasMovRV = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES
                    cmov = 0
                    

            if CTRV !=ctrv:
                print("Dto verde",CTRV)
                verde = open("C:/Users/Neftali/Desktop/Comunicación esp/Verde/ordenv.txt","w")
                verde.write(str(CTRV))
                verde.close()
                if CTRV == 1:
                    time.sleep(.5)
                ctrv = CTRV
            x11 = x1
            x21 = x2

            

            '''rob2Mov = open("C:/Users/Neftali/Desktop/memoria parte final/Constantes/Movimiento/Rob2Mov.txt","w")
            Rob2Mov = rob2Mov.read()
            rob2Mov.close()

            if Rob2Mov == '3':##mueve azul y naranjo
                Dis1,xfra,yfra,xfrr,yfrr = Discrim2(x1,y1,x2,y2,ax1,ay1,rx1,ry1)
                
                if Dis1 == 1:
                    print("Azul a punto 1 y Naranjo a punto 2")
                if Dis1 == 2:
                    print("Azul a punto 2 y Naranjo a punto 2")
                

            elif Rob2Mov == '4':## mueve azul y verde
                Dis2 = Discrim2(x1,y1,x2,y2,ax1,ay1,vx1,vy1)

                if Dis2 == 1:
                    print("Azul a punto 1 y Verde a punto 2")
                    if
                if Dis2 == 2:
                    print("Azul a punto 2 y Verde a punto 2")

            elif Rob2Mov == '5':## mueve naranjo y verde
                Dis3 = Discrim2(x1,y1,x2,y2,rx1,ry1,vx1,vy1)

                if Dis3 == 1:
                    print("Naranjo a punto 1 y Verde a punto 2")
                if Dis3 == 2:
                    print("Naranjo a punto 2 y Verde a punto 2")'''
            

        elif Robmov == '5':##mover todos
            xfra,yfra,xfrr,yfrr,xfrv,yfrv = Discrim3(x1,y1,x2,y2,x3,y3,ax1,ay1,rx1,ry1,vx1,vy1)

            VecAz = ((xfra-ax1)**2+(yfra-ay1)**2)**(1/2) #Distancia entre puntos
            VecNa = ((xfrr-rx1)**2+(yfrr-ry1)**2)**(1/2)
            VecVe = ((xfrv-vx1)**2+(yfrv-vy1)**2)**(1/2)

            if la ==1:
                print("Vector azul: ",VecAz)
                print("Vector Rojo: ",VecNa)
                print("Vector Verde: ",VecVe)
                la =0
            if x11 != x1 and x21 != x2:
                c21 = 1
                c22 = 1
                c23 = 1

            if VecAz >= 12 :
                #CTRA,DifAz,ca,ConsMoA = DatoPWM(x1,y1,ax1,ay1,cx1,cy1,ca,ConsMoA)
                if c21 == 1:
                    if xfra == x1:
                        print("Robot azul a punto 1")
                    elif xfra == x2:
                        print("Robot azul a punto 2")
                    else:
                        print("Robot azul a punto 3")
                    c21 = 0
                    

                
            if VecNa >= 12 :
                #CTRN,DifNa,cn,ConsMoN = DatoPWM(x1,y1,ax1,ay1,cx1,cy1,cn,ConsMoN)
                if c22 == 1:
                    if xfrr == x1:
                        print("Robot rojo a punto 1")
                    elif xfrr == x2:
                        print("Robot rojo a punto 2")
                    else:
                        print("Robot rojo a punto 3")
                    c22 = 0



            if VecVe >= 12 :
                #CTRA,DifVe,cv,ConsMoV = DatoPWM(x1,y1,ax1,ay1,cx1,cy1,ca,ConsMoV)
                if c23 == 1:
                    if xfrv == x1:
                        print("Robot verde a punto 1")
                    elif xfrv == x2:
                        print("Robot verde a punto 2")
                    elif xfrv == x3:
                        print("Robot verde a punto 3")
                    c23 = 0
            x12 = x1
            x22 = x2
            x32 = x3

