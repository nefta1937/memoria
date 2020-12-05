import math
import os
from io import open
import time
import prueba

ax1=ay1=cx1=cy1=vx1=vy1=amx1=amy1=rx1=ry1=rox1=roy1=0
c=0
ConsMoV = 1
ctrv=1000

while(1):
    per = open("C:/Users/Neftali/Desktop/Universidad/Swarm Robot/Reconocimiento de imagen/Python/per.txt","r")
    p = per.read()
    per.close()

    if p == '1' :
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

        #prueba.sayhello()
    
    ###pendientes###
        AlpRA = math.degrees(math.atan2((cy1-ay1),(cx1-ax1)))*-1
        AlpRV = math.degrees(math.atan2((amy1-vy1),(amx1-vx1)))*-1
        if AlpRV >=0:
            AlpRV = AlpRV
        else:
            AlpRV = 360 + AlpRV
        AlpRN = math.degrees(math.atan2((roy1-ry1),(rox1-rx1)))*-1

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
            #print("La Distancia del robot azul al punto es: ",VecAz,"\nLa Distancia del robot naranjo al punto es: ",VecNa,"\nLa Distancia del robot verde al punto es: ",VecVe)
            ############################################################
            if VecAz <= VecNa and VecAz <=VecVe and VecAz <= VecVe:
                print("El robot azul está más cerca")
                AlpRAF = math.degrees(math.atan((y1-ay1),(x1-ax1)))*-1
                if AlpRAF >=0:
                    AlpRAF = AlpRAF
                else:
                    AlpRAF = 360 + AlpRAF
                if VecAz > 15:
                    print("Comenzar movimiento")
                    print(AlpRA)
                    print(AlpRAF)
            ##movimiento del robot
                
                    if AlpRA < (AlpRAF+5) and AlpRA > (AlpRAF-5):
                        print("Moverse derecho")
                        ConsGir = 1
                        CTRA = 20                        
                    else:
                        ConsGir = 0
                    ##Corregir la dirección del robot

                    if AlpRA < AlpRAF and ConsGir == 0:
                        print("Girar sentido anti horario")
                        CTRA = 320  
                    elif AlpRA > AlpRAF and ConsGir == 0:
                        print("Girar sentido horario")
                        CTRA = 220  
                    
                else :
                    print("UI puede volver a funcionar ")
                    CTRA = 0
                    PasMovRA = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES

                
            ###########################################################        
            elif VecNa <= VecVe and VecNa <=VecAz:
                print("El robot naranjo está más cerca")
                AlpRNF = math.degrees(math.atan2((y1-ry1),(x1-rx1)))*-1
                if AlpRNF >=0:
                    AlpRNF = AlpRNF
                else:
                    AlpRNF = 360 + AlpRNF

                if VecAz > 15:
                    print("Comenzar movimiento")
                    print(AlpRN)
                    print(RadRN)
                    print(AlpRNF)
            ##movimiento del robot
                
                    if AlpRN < (AlpRNF+15) and AlpRN > (AlpRNF-15):
                        print("Moverse derecho")
                        ConsGir = 1
                        CTRN = 225

                    else:
                        ConsGir = 0
                    ##Corregir la dirección del robot

                    if AlpRN < AlpRNF and ConsGir == 0:
                        print("Girar sentido anti horario")
                        CTRN = 15
                    elif AlpRN > AlpRNF and ConsGir == 0:
                        print("Girar sentido horario")
                        CTRN = 116
                else :
                    print("UI puede volver a funcionar ")
                    CTRN = 0
                    PasMovRN = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES



            #####################################################   
            else:
                AlpRVF = math.degrees(math.atan2((y1-vy1),(x1-vx1)))*-1
                if AlpRVF >=0:
                    AlpRVF = AlpRVF
                else:
                    AlpRVF = 360 + AlpRVF

                DifVe = AlpRV - AlpRVF
                if DifVe >=0:
                    DifVe = DifVe
                else:
                    DifVe = 360 + DifVe
                print("Robot ",AlpRV)
                print("Punto ",AlpRVF)
                print("Diferencia ",DifVe)
                time.sleep(.8)
                if VecVe > 15:
            ##movimiento del robot
                
                    if DifVe < 7.5 or DifVe > 172.5 and ConsMoV == 1 :
                        if c!=1:
                            print("Moverse derecho")
                            c=1
                            CTRV = 0
                        else: 
                            CTRV = 225
                    elif abs(DifVe) > 170 and DifVe < 190 and ConsMoV == 1 :
                        if c!=4:
                            print("Moverse derecho")
                            c=4
                            CTRV = 0
                        else: 
                            CTRV = 325

                    else:
                        ConsMoV = 0
                    ##Corregir la dirección del robot

                    if DifVe < -10 and ConsMoV == 0:
                        if c!=2:
                            print("Girar sentido anti horario")
                            c=2
                            CTRV = 0
                        else:
                            CTRV = 5
                    elif DifVe > 10 and ConsMoV == 0:
                        if c!=3:
                            print("Girar sentido horario")
                            c=3
                            CTRV = 0
                        else:
                            CTRV = 106
                    else:
                        ConsMoV = 1
                else :
                    print("UI puede volver a funcionar ")
                    CTRV = 0
                    PasMovRV = 0 ##PASO A MOVIMIENTO A ROBOT BLOQUEADO HASTA QUE SE CAMBIEN COORDENADAS FINALES

